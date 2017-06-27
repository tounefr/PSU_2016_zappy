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
    init_map(&server->map);
    server->clients_per_team = DEFAULT_CLIENTS_PER_TEAM;
}

char listen_server(t_server *server)
{
    if (-1 == (server->server_fd = socket_init()))
        return 0;
    if (!socket_listen(server->server_fd, "0.0.0.0", &server->listen_port))
        return 0;
    return 1;
}

char update(t_server *server, struct timeval *last_tick)
{
    int i;
    t_client *client;

    if (is_next_cycle(server, last_tick)) {
        printf("cycle %d\n", server->cur_cycle);
        if (server->cur_cycle == 1 || (server->cur_cycle % 600) == 0)
            generate_resources(server);
        for (i = 0; i < MAX_CLIENTS; i++) {
            client = &server->clients[i];
            if (client->socket_fd == -1)
                continue;
            client->life_cycles--;
            if ((client->life_cycles % 126) == 0)
                client->inventory[TYPE_FOOD]--;
            if (check_player_dead(server, client))
                continue;
            hatch_eggs(server, client);
            if (client->remain_cycles == -1)
                packet_pre_cycle(server, client);
            else if (client->remain_cycles > 1)
                client->remain_cycles--;
            else if (client->cur_packet)
                packet_post_cycle(server, client);
        }
    }
    return 1;
}

char main_loop(t_server *server)
{
    int nfds;
    fd_set fds;
    int selectrv;
    struct timeval timeout;
    struct timeval last_tick;

    if (!listen_server(server))
        return 0;
    gettimeofday(&last_tick, 0);
    while (1) {
        select_init(server, &nfds, &fds, &timeout);
        if ((selectrv = select(nfds, &fds, NULL, NULL, &timeout)) == -1)
            return exit_error(0, "select error : %s\n", strerror(errno));
        if (selectrv > 0 && !on_select_data(server, &fds))
            return 0;
        if (!update(server, &last_tick))
            return 0;
    }
}
