/*
** commands3.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Fri Jun 23 15:00:53 2017 Thomas HENON
** Last update Tue Jun 27 11:31:17 2017 arsene
*/

#include "server.h"

char    onLeftPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)packet;
    if (client->orientation == ORIENT_WEST)
        client->orientation = ORIENT_SOUTH;
    else if (client->orientation == ORIENT_EAST)
        client->orientation = ORIENT_NORTH;
    else if (client->orientation == ORIENT_NORTH)
        client->orientation = ORIENT_WEST;
    else if (client->orientation == ORIENT_SOUTH)
        client->orientation = ORIENT_EAST;
    packet_send(client, "ok\n");
    send_gui_packet(server, "ppo %d %d %d %d\n",
                    client->num, client->pos.x, client->pos.y, client->orientation);
    return 1;
}

char    onLookPacket(t_server *server, t_client *client, char *packet)
{
  (void)server;
  (void)client;
  (void)packet;

  return 1;
}

char on_welcome(t_server *server, t_client *client, char *packet) {
    if (!strcmp(packet, "GRAPHIC")) {
        client->is_gui = 1;
        server->gui_client = client;
        packet_send(client, "msz %d %d\n",
                    server->map.width, server->map.height);
        packet_send(client, "sgt %d\n", (int) server->freq);
        gui_send_map_content(server, client);
        gui_send_teams(server, client);
    } else {
        client->num = server->client_lastnum++;
        if (!client_assign_team(server, client, packet))
            return packet_send(client, "ko\n");
        if (!egg_pending_client(server, client)) {
            if (client->team->slots - 1 < 0)
                return packet_send(client, "ko\n");
            else
                client->team->slots--;
        }
        packet_send(client, "%d\n", client->team->slots);
        packet_send(client, "%d %d\n",
                server->map.width, server->map.height);
    }
    return 1;
}
