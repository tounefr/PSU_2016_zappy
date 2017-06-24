/*
** select.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:01:02 2017 Thomas HENON
** Last update Fri Jun 23 15:01:02 2017 Thomas HENON
*/

#include <sys/select.h>
#include <stdio.h>
#include "server.h"
#include "network.h"

void select_init(t_server *server, int *nfds,
                 fd_set *fds, struct timeval *timeout)
{
    int i;

    *nfds = server->server_fd + 1;
    FD_ZERO(fds);
    timeout->tv_sec = 0;
    timeout->tv_usec = 10000; //10ms
    FD_SET(server->server_fd, fds);
    for (i = 0; i < MAX_CLIENTS; i++) {
        if (server->clients[i].socket_fd == -1)
            continue;
        FD_SET(server->clients[i].socket_fd, fds);
        if (server->clients[i].socket_fd > *nfds - 1)
            *nfds = server->clients[i].socket_fd + 1;
    }
}

char on_select_data(t_server *server, fd_set *fds)
{
    int i;

    if (FD_ISSET(server->server_fd, fds))
        on_new_client(server);
    for (i = 0; i < MAX_CLIENTS; i++) {
        if (server->clients[i].socket_fd == -1)
            continue;
        if (FD_ISSET(server->clients[i].socket_fd, fds)) {
            if (!on_available_data(server, &server->clients[i]))
                close_client_connection(&server->clients[i]);
        }
    }
    return 1;
}
