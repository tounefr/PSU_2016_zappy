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

float cpt_cycle_time(t_server *server)
{
    return (1.0f / server->freq) * 1000; // ms
}

void init_server(t_server *server)
{
    int i;

    for (i = 0; i < MAX_TEAMS; i++)
        memset(&server->teams[i], 0, sizeof(server->teams));
    for (i = 0; i < MAX_CLIENTS; i++)
        init_client(&server->clients[i]);
    server->freq = DEFAULT_FREQUENCY;
    server->listen_port = DEFAULT_LISTEN_PORT;
    server->cycle_time = cpt_cycle_time(server);
    server->cur_cycle = 0;
    server->gui_client = NULL;
    server->client_lastnum = 1;
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
