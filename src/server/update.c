/*
** update.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Thu Jun 29 20:28:26 2017 Thomas HENON
** Last update Sun Jul  2 17:16:15 2017 arsene
*/

#include "server.h"

char update_client(t_server *server, t_client *client)
{
    t_callback *callback;

    if (client->socket_fd == -1 || client->is_gui)
        return 0;
    if (!handle_pre_packet(server, client)) {
        on_exit_client(server, client);
        return 0;
    }
    if ((callback = get_callback(client, onPlayerDead))) {
        callback->cycles--;
        client->inventory[TYPE_FOOD] = callback->cycles / CYCLES_PER_LIFE_UNIT;
    }
    if (!handle_post_packet(server, client)) {
        on_exit_client(server, client);
        return 0;
    }
    return 1;
}

char update(t_server *server, struct timeval *last_tick)
{
  int i;
  int nb_clients;
  t_client *client;

    if (is_next_cycle(server, last_tick)) {
        if (server->cur_cycle == 1)
            generate_resources(server);
        nb_clients = 0;
        for (i = 0; i < MAX_CLIENTS; i++) {
            client = &server->clients[i];
            if (client->socket_fd != -1 && !client->is_gui)
                nb_clients++;
            update_client(server, client);
        }
    }
  return 1;
}

char main_loop(t_server *server)
{
    int nfds;
    fd_set read_fds;
    fd_set write_fds;
    int selectrv;
    struct timeval timeout;
    struct timeval last_tick;

    if (!listen_server(server))
        return 0;
    gettimeofday(&last_tick, 0);
    while (1) {
        select_init(server, &nfds, &read_fds, &write_fds);
        timeout.tv_sec = 0;
        timeout.tv_usec = server->cycle_time;
        if ((selectrv = select(nfds, &read_fds, &write_fds, NULL,
                               &timeout)) == -1)
            return exit_error(0, "select error : %s\n", strerror(errno));
        if (selectrv > 0 && !on_select_read_data(server, &read_fds))
            return 0;
        if (selectrv > 0 && !on_select_write_data(server, &write_fds))
            return 0;
        if (!update(server, &last_tick))
            return 0;
    }
}
