/*
** commands3.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Fri Jun 23 15:00:53 2017 Thomas HENON
** Last update Wed Jun 28 14:04:24 2017 arsene
*/

#include <sys/types.h>
#include <unistd.h>
#include "server.h"

char    onLeftPacket(t_server *server, t_client *client, char *packet)
{
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
                    client->num, client->pos.x,
                    client->pos.y, client->orientation);
    return 1;
}

char    onLookPacket(t_server *server, t_client *client, char *packet)
{
  (void)packet;
  look(client, server);
  return 1;
}

static char on_graphic_welcome(t_server *server,
                               t_client *client,
                               char *packet)
{
    (void)packet;
    server->gui_client = client;
    client->is_gui = 1;
    send_gui_packet(server, "msz %d %d\n",
                    server->map.width, server->map.height);
    send_gui_packet(server, "sgt %d\n", (int) server->freq);
    gui_send_map_content(server);
    gui_send_teams(server);
    send_gui_players_connected(server);
    return 1;
}

static char on_client_welcome(t_server *server,
                              t_client *client,
                              char *packet)
{
    static int max_client_num = 1;

    client->num = max_client_num++;
    if (!client_assign_team(server, client, packet))
        return packet_send(client, "ko\n");
    if (client->team->slots - 1 < 0)
        return packet_send(client, "ko\n");
    else
        client->team->slots--;
    client->pos.x = my_rand(0, server->map.width - 1);
    client->pos.y = my_rand(0, server->map.height - 1);
    remove_hatched_egg(server, client);
    server->map.cases[get_pos(server, &client->pos)][TYPE_PLAYER]++;
    packet_send(client, "%d\n", client->team->slots);
    packet_send(client, "%d %d\n",
                server->map.width, server->map.height);
    send_gui_packet(server, "pnw %d %d %d %d %d %s\n",
                    client->num, client->pos.x,
                    client->pos.y, client->orientation,
                    client->level, client->team->name);
    client->in_game = 1;
    return 1;
}

char on_welcome(t_server *server, t_client *client, char *packet) {
    if (!strcmp(packet, "GRAPHIC"))
        return on_graphic_welcome(server, client, packet);
    else
        return on_client_welcome(server, client, packet);
}
