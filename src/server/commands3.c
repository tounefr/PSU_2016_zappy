/*
** commands3.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Fri Jun 23 15:00:53 2017 Thomas HENON
** Last update Sun Jun 25 16:09:41 2017 arsene
*/

#include "server.h"

char    onLeftPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)packet;
    if (client->orientation == ORIENT_OUEST)
        client->orientation = ORIENT_SOUTH;
    else if (client->orientation == ORIENT_EST)
        client->orientation = ORIENT_NORTH;
    else if (client->orientation == ORIENT_NORTH)
        client->orientation = ORIENT_OUEST;
    else if (client->orientation == ORIENT_SOUTH)
        client->orientation = ORIENT_EST;
    return packet_send(client->socket_fd, "ok\n");
}

char    onLookPacket(t_server *server, t_client *client, char *packet)
{
  (void)server;
  (void)client;
  (void)packet;

  return 1;
}

char on_welcome(t_server *server, t_client *client, char *packet) {
    int client_in_team_left;

    if (!strcmp(packet, "GRAPHIC")) {
        client->is_gui = 1;
        dprintf(client->socket_fd, "msz %d %d\n", server->map.width, server->map.height);
        dprintf(client->socket_fd, "sgt %d\n", (int) server->freq);
        gui_send_map_content(server, client);
        gui_send_teams(server, client);
    } else {
        if (!client_assign_team(server, client, packet))
            return dprintf(client->socket_fd, "ko\n");
        client->team->slots--;
        dprintf(client->socket_fd, "%d\n", client->team->slots);
        dprintf(client->socket_fd, "%d %d\n",
                server->map.width, server->map.height);
    }
    return 1;
}
