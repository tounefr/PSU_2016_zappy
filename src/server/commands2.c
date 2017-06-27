/*
** commands2.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Fri Jun 23 15:00:46 2017 Thomas HENON
** Last update Tue Jun 27 11:30:33 2017 arsene
*/

#define _GNU_SOURCE
#include <stdio.h>
#include "server.h"

char    onConnectNbrPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)client;
    (void)packet;
    packet_send(client->socket_fd, "%d\n", client->team->slots);
    return 1;
}

char    onBroadcastPacket(t_server *server, t_client *client, char *packet)
{
    int i;
    int i2;
    char *msg;
    int k;

    k = 1; //TODO
    if (strlen(packet) < strlen("Broadcast "))
        return packet_send(client->socket_fd, "ko\n");
    msg = packet + strlen("Broadcast ");
    for (i = 0; i < MAX_CLIENTS; i++) {
        if (server->clients[i].socket_fd == -1)
            continue;
        if (&server->clients[i] == client)
            continue;
        if (server->clients[i].team == client->team) {
            packet_send(server->clients[i].socket_fd,
                        "message %d, %s\n", k, msg);
        }
    }
    return packet_send(client->socket_fd, "ok\n");
}

char    onInventoryPacket(t_server *server, t_client *client, char *packet)
{
    char *buffer;

    if (asprintf(&buffer,
             "[ linemate %d, deraumere %d, sibur %d, "
            "mendiane %d, phiras %d, thystame %d, food %d ]\n",
             client->inventory[TYPE_LINEMATE], client->inventory[TYPE_DERAUMERE],
             client->inventory[TYPE_SIBUR], client->inventory[TYPE_MENDIANE],
             client->inventory[TYPE_PHIRAS], client->inventory[TYPE_THYSTAME],
             client->inventory[TYPE_FOOD]) == -1)
        return exit_error(0, "malloc error\n");
    packet_send(client->socket_fd, "%s", buffer);
    send_gui_packet(server, "pin %d %d %d %d %d %d %d %d %d %d\n",
        client->num, client->pos.x, client->pos.y,
                    client->inventory[TYPE_FOOD], client->inventory[TYPE_LINEMATE],
                    client->inventory[TYPE_DERAUMERE], client->inventory[TYPE_SIBUR],
                    client->inventory[TYPE_MENDIANE], client->inventory[TYPE_PHIRAS],
                    client->inventory[TYPE_THYSTAME]);
    free(buffer);
    return 1;
}

char    onForwardPacket(t_server *server, t_client *client, char *packet)
{
    (void)packet;
    (void)server;
    if (client->orientation == ORIENT_WEST)
        client->pos.x--;
    if (client->orientation == ORIENT_EAST)
        client->pos.x++;
    if (client->orientation == ORIENT_NORTH)
        client->pos.y--;
    if (client->orientation == ORIENT_SOUTH)
        client->pos.y++;
    if (client->pos.y < 0)
        client->pos.y = server->map.height - 1;
    if (client->pos.x < 0)
        client->pos.x = server->map.width - 1;
    if (client->pos.y >= server->map.height)
        client->pos.y = 0;
    if (client->pos.x >= server->map.width)
        client->pos.x = 0;
    send_gui_packet(server, "ppo %d %d %d %d\n",
                    client->num, client->pos.x, client->pos.y, client->orientation);
    return packet_send(client->socket_fd, "ok\n");
}

char    onRightPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)packet;
    if (client->orientation == ORIENT_WEST)
        client->orientation = ORIENT_NORTH;
    else if (client->orientation == ORIENT_EAST)
        client->orientation = ORIENT_SOUTH;
    else if (client->orientation == ORIENT_NORTH)
        client->orientation = ORIENT_EAST;
    else if (client->orientation == ORIENT_SOUTH)
        client->orientation = ORIENT_WEST;
    packet_send(client->socket_fd, "ok\n");
    send_gui_packet(server, "ppo %d %d %d %d\n",
                    client->num, client->pos.x, client->pos.y, client->orientation);
    return 1;
}
