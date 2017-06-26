/*
** incantation.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Mon Jun 26 11:25:50 2017 Thomas HENON
** Last update Mon Jun 26 11:25:50 2017 Thomas HENON
*/

#include <stdio.h>
#include "server.h"

char checkIncantationPacket(t_server *server, t_client *client, char *packet)
{
    int i;
    t_incantation *incantation;

    if (client->level > 7)
        return 0;
    incantation = &g_incantations[client->level - 1];
    int i2 = client->pos.x + client->pos.y * server->map.height;
    for (i = 0; i < RESOURCES_NBR_TYPES; i++) {
        if (server->map.cases[i2][i] != client->inventory[i]) {
            printf("not enough ressources\n");
            return 0;
        }
    }
    if (client->level + 1 > MAX_LEVEL)
        return 0;
    return 1;
}

char    onPreIncantationPacket(t_server *server, t_client *client, char *packet)
{
    if (!checkIncantationPacket(server, client, packet))
        return packet_send(client->socket_fd, "ko\n");
    return packet_send(client->socket_fd, "Elevation underway\n");
}

char    onPostIncantationPacket(t_server *server, t_client *client, char *packet)
{
    if (!checkIncantationPacket(server, client, packet))
        return packet_send(client->socket_fd, "ko\n");
    client->level++;
    return packet_send(client->socket_fd, "Current level: %d\n", client->level);
}
