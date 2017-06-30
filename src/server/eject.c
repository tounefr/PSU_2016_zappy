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
        dest.y = abs(dest.y - 1) % server->map.height;
        if (dest.y < 0)
            dest.y = server->map.height - 1;
    }
    else if (client->orientation == ORIENT_SOUTH)
        dest.y = abs(dest.y + 1) % server->map.height;
    else if (client->orientation == ORIENT_EAST) {
        dest.x = abs(dest.x - 1) % server->map.width;
        if (dest.x < 0)
            dest.x = server->map.width - 1;
    }
    else if (client->orientation == ORIENT_WEST)
        dest.x = abs(dest.x + 1) % server->map.width;
    return dest;
}

char    onEjectPacket(t_server *server, t_client *client, char *packet)
{
    int i;
    int k;
    t_pos dest;

    (void)packet;
    k = 1;
    for (i = 0; i < MAX_CLIENTS; i++) {
        if (server->clients[i].socket_fd == -1 ||
                &server->clients[i] == client)
            continue;
        dest = get_dest_case(server, client);
        server->clients[i].pos = dest;
        packet_send(&server->clients[i], "eject: %d\n", k);
        send_gui_packet(server, "ppo %d %d %d %d\n",
                        server->clients[i].num, server->clients[i].pos.x,
                        server->clients[i].pos.y, server->clients[i].orientation);
    }
    return 1;
}
