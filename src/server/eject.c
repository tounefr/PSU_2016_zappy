/*
** eject.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Tue Jun 27 16:49:56 2017 Thomas HENON
** Last update Tue Jun 27 16:49:57 2017 Thomas HENON
*/

#include "server.h"

static t_pos get_dest_case(t_server *server, t_client *client)
{
    t_pos dest;

    dest = client->pos;
    if (client->orientation == ORIENT_NORTH) {
        dest.y = dest.y - 1;
        if (dest.y < 0)
            dest.y = server->map.height - 1;
    }
    else if (client->orientation == ORIENT_SOUTH) {
        dest.y = dest.y + 1;
        if (dest.y >= server->map.height)
            dest.y = 0;
    }
    else if (client->orientation == ORIENT_EAST) {
        dest.x = dest.x + 1;
        if (dest.x >= server->map.width)
            dest.x = 0;
    }
    else if (client->orientation == ORIENT_WEST) {
        dest.x = dest.x - 1;
        if (dest.x < 0)
            dest.x = server->map.width - 1;
    }
    return dest;
}

char    onEjectPacket(t_server *server, t_client *client, char *packet)
{
    int i;
    int k;
    t_pos dest;
    t_client *c;

    (void)packet;
    k = 1;
    dest = get_dest_case(server, client);
    for (i = 0; i < MAX_CLIENTS; i++) {
         c = &server->clients[i];
        if (c->socket_fd == -1 || c == client || c->is_gui)
            continue;
        if (c->pos.x != client->pos.x || c->pos.y != client->pos.y)
            continue;
        c->pos = dest;
        packet_send(c, "eject: %d\n", k);
        send_gui_packet(server, "ppo %d %d %d %d\n",
            c->num, c->pos.x, c->pos.y, c->orientation);
    }
    return 1;
}
