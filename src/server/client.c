/*
** client.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:01:11 2017 Thomas HENON
** Last update Fri Jun 23 15:01:11 2017 Thomas HENON
*/

#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include "server.h"

void init_client(t_client *client)
{
    int i;

    client->socket_fd = -1;
    memset(&client->buffer, 0, sizeof(client->buffer));
    client->num = -1;
    client->pos.x = 0;
    client->pos.y = 0;
    client->recv_packet_i = 0;
    client->is_gui = 0;
    client->orientation = ORIENT_SOUTH;
    client->cur_packet = NULL;
    client->level = 1;
    client->team = NULL;
    for (i = 0; i < MAX_PENDING_PACKETS; i++)
        memset(&client->pending_packets[i], 0, BUFFER_SIZE);
    client->remain_cycles = -1;
    for (i = 0; i < RESOURCES_NBR_TYPES; i++)
        client->inventory[i] = 0;
    client->inventory[TYPE_FOOD] = PLAYER_LIFE_UNITS;
    client->life_cycles = client->inventory[TYPE_FOOD] * CYCLES_PER_LIFE_UNIT;
    for (i = 0; i < MAX_EGGS_PER_CLIENT; i++)
        memset(&client->eggs[i], 0, sizeof(t_egg));
}


char on_new_client(t_server *server)
{
    int i;
    int flags;
    int fd;

    i = 0;
    for (i = 0; i < MAX_CLIENTS; i++) {
        if (server->clients[i].socket_fd == -1) {
            server->clients[i].socket_fd = socket_accept(server->server_fd);
            fd = server->clients[i].socket_fd;
            flags = fcntl(fd, F_GETFL, 0);
            if (-1 == fcntl(fd, F_SETFL, flags | O_NONBLOCK))
                return exit_error(0, "fcntl error : %s\n", strerror(errno));
            return packet_send(server->clients[i].socket_fd, "BIENVENUE\n");
        }
    }
    return exit_error(0, "error : no slots available\n");
}

void close_client_connection(t_client *client)
{
    socket_close(client->socket_fd);
    init_client(client);
}
