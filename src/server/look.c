/*
** look.c for look in /home/arsene/Desktop/{EPITECH}/PSU/PSU_2016_zappy/src/server
**
** Made by arsene
** Login   <arsene@arsene-HP-EliteBook-840-G2>
**
** Started on  Mon Jun 26 14:18:29 2017 arsene
** Last update Sat Jul  1 12:46:23 2017 arsene
*/

#include <stdlib.h>
#include <string.h>
#include "server.h"

void look(t_client *client, t_server *server)
{
    t_look see;

    init_look(&see);
    if (client->orientation == ORIENT_NORTH)
        lookUp(server, client, &see);
    if (client->orientation == ORIENT_SOUTH)
        lookDown(server, client, &see);
    if (client->orientation == ORIENT_EAST)
        lookRight(server, client, &see);
    if (client->orientation == ORIENT_WEST)
        lookLeft(server, client, &see);
    convertView(client, &see);
}
