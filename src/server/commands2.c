/*
** commands2.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:00:46 2017 Thomas HENON
** Last update Fri Jun 23 15:00:47 2017 Thomas HENON
*/

#include "server.h"

char    onConnectNbrPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)client;
    (void)packet;
    //TODO:
/*    client_in_team_left = server->clients_per_team -
                          clients_in_team((t_client*)&server->clients, client->team_i);
    dprintf(client->socket_fd, "%d\n", client_in_team_left);*/
    return 1;
}

char    onBroadcastPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)client;
    (void)packet;
    return 1;
}

char    onInventoryPacket(t_server *server, t_client *client, char *packet)
{
    char buffer[1000];

    (void)packet;
    (void)server;
    memset(&buffer, 0, sizeof(buffer));
    snprintf((char*)&buffer, (size_t)(sizeof(buffer) - 1),
             "[ linemate %d, deraumere %d, sibur %d, "
             "mendiane %d, phiras %d, thystame %d, food %d ]\n",
        client->inventory[TYPE_LINEMATE], client->inventory[TYPE_DERAUMERE],
         client->inventory[TYPE_SIBUR], client->inventory[TYPE_MENDIANE],
         client->inventory[TYPE_PHIRAS], client->inventory[TYPE_THYSTAME],
        client->inventory[TYPE_FOOD]);
    dprintf(client->socket_fd, "%s", (char*)&buffer);
    return 1;
}

char    onForwardPacket(t_server *server, t_client *client, char *packet)
{
    (void)packet;
    (void)server;
    if (client->orientation == ORIENT_OUEST)
        client->pos.x--;
    if (client->orientation == ORIENT_EST)
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
    packet_send(client->socket_fd, "ok\n");
    return 1;
}

char    onRightPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)packet;
    if (client->orientation == ORIENT_OUEST)
        client->orientation = ORIENT_NORTH;
    else if (client->orientation == ORIENT_EST)
        client->orientation = ORIENT_SOUTH;
    else if (client->orientation == ORIENT_NORTH)
        client->orientation = ORIENT_EST;
    else if (client->orientation == ORIENT_SOUTH)
        client->orientation = ORIENT_OUEST;
    packet_send(client->socket_fd, "ok\n");
    return 1;
}
