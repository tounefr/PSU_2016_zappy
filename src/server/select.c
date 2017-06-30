/*
** select.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:01:02 2017 Thomas HENON
** Last update Fri Jun 23 15:01:02 2017 Thomas HENON
*/

#include <sys/types.h>
#include <sys/socket.h>
#include <sys/select.h>
#include <stdio.h>
#include "server.h"

void select_init(t_server *server, int *nfds,
                 fd_set *read_fds, fd_set *write_fds)
{
    int i;
    t_client *client;

    *nfds = server->server_fd + 1;
    FD_ZERO(read_fds);
    FD_ZERO(write_fds);
    FD_SET(server->server_fd, read_fds);
    for (i = 0; i < MAX_CLIENTS; i++) {
        client = &server->clients[i];
        if (server->clients[i].socket_fd == -1)
            continue;
        FD_SET(server->clients[i].socket_fd, read_fds);
        if (client->write_packets)
            FD_SET(server->clients[i].socket_fd, write_fds);
        if (server->clients[i].socket_fd > *nfds - 1)
            *nfds = server->clients[i].socket_fd + 1;
    }
}

char on_select_read_data(t_server *server, fd_set *fds)
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

char on_select_write_data(t_server *server, fd_set *fds)
{
    int i;
    t_client *client;
    char *packet;

    for (i = 0; i < MAX_CLIENTS; i++) {
        client = &server->clients[i];
        if (client->socket_fd == -1)
            continue;
        if (FD_ISSET(client->socket_fd, fds)) {
            if (!client->write_packets)
                continue;
            packet = (char*)generic_list_pop(&client->write_packets);
            printf("Send>> %s", packet);
            if (-1 == send(client->socket_fd, packet, strlen(packet), 0)) {
                exit_error(0, "%s\n", strerror(errno));
                continue;
            }
            free(packet);
        }
    }
    return 1;
}
