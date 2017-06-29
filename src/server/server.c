/*
** server.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:01:25 2017 Thomas HENON
** Last update Fri Jun 23 15:01:26 2017 Thomas HENON
*/

#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>
#include "server.h"

void init_server(t_server *server)
{
    int i;

    for (i = 0; i < MAX_TEAMS; i++)
        memset(&server->teams[i], 0, sizeof(server->teams));
    for (i = 0; i < MAX_CLIENTS; i++)
        init_client(&server->clients[i]);
    server->freq = DEFAULT_FREQUENCY;
    server->listen_port = DEFAULT_LISTEN_PORT;
    server->cycle_time = (1.0f / server->freq) * 1000; // ms
    server->cur_cycle = 0;
    server->gui_client = NULL;
    server->client_lastnum = 1;
    init_map(&server->map);
    server->clients_per_team = DEFAULT_CLIENTS_PER_TEAM;
    memset(&server->eggs, 0, sizeof(server->eggs));
}

char listen_server(t_server *server)
{
    if (-1 == (server->server_fd = socket_init()))
        return 0;
    if (!socket_listen(server->server_fd, "0.0.0.0", &server->listen_port))
        return 0;
    return 1;
}

char update_client(t_server *server, t_client *client)
{
    if (client->socket_fd == -1 || client->is_gui)
        return 0;
    if (!client->cur_packet) {
        if (!handle_pre_packet(server, client)) {
            on_exit_client(server, client);
            return 0;
        }
    }
    client->life_cycles--;
    if ((client->life_cycles % 126) == 0)
        client->inventory[TYPE_FOOD]--;
    /*if (check_player_dead(server, client))
        continue;*/
    hatch_eggs(server, client);
    if (!handle_post_packet(server, client)) {
        on_exit_client(server, client);
        return 0;
    }
    return 1;
}

char update(t_server *server, struct timeval *last_tick)
{
    int i;
    t_client *client;

    if (is_next_cycle(server, last_tick)) {
//        printf("cycle %d\n", server->cur_cycle);
        if (server->cur_cycle == 1 || (server->cur_cycle % 1200) == 0)
            generate_resources(server);
        for (i = 0; i < MAX_CLIENTS; i++) {
            client = &server->clients[i];
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
        if ((selectrv = select(nfds, &read_fds,
                               &write_fds, NULL, &timeout)) == -1)
            return exit_error(0, "select error : %s\n", strerror(errno));
        if (selectrv > 0 && !on_select_read_data(server, &read_fds))
            return 0;
        if (selectrv > 0 && !on_select_write_data(server, &write_fds))
            return 0;
        if (!update(server, &last_tick))
            return 0;
    }
}
