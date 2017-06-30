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
    int i2;
    int pos;
    t_incantation *incantation;

    (void)packet;
    if (client->level > 7)
        return 0;
    pos = client->pos.x + client->pos.y * server->map.height;
    incantation = &get_g_incantations()[client->level - 1];
    if (get_nb_players_lvl(server, client->level) != incantation->nb_players)
        return exit_error(0, "no enought players with same level to levelup\n");
    for (i = 0 ; i < RESOURCES_NBR_TYPES; i++) {
        if (server->map.cases[pos][i] < incantation->type[i])
            return exit_error(0, "not enough ressources\n");
    }
    if (client->level + 1 > MAX_LEVEL)
        return 0;
    return 1;
}

char    onPreIncantPacket(t_server *server,
                               t_client *client,
                               char *packet)
{
    if (!checkIncantationPacket(server, client, packet)) {
        send_gui_packet(server, "pie %d %d %d\n",
                        client->pos.x, client->pos.y, 0);
        return packet_send(client, "ko\n");
    }
    return packet_send(client, "Elevation underway\n");
}

static char decreaseResourcesOnMap(t_server *server,
                                   t_pos *pos,
                                   t_incantation *incantation)
{
    int i;
    int p;

    for (i = 0; i < RESOURCES_NBR_TYPES; i++) {
        if (!is_stone(i))
            continue;
        p = pos->y * server->map.height + pos->x;
        server->map.cases[p][i] -= incantation->type[i];
    }
}

static char onLevelUp(t_server *server, t_client *client)
{
    t_incantation *incantation;

    incantation = &get_g_incantations()[client->level - 1];
    client->level++;
    send_gui_packet(server, "plv %d %d\n", client->num, client->level);
    send_gui_packet(server, "pie %d %d %d\n",
                    client->pos.x, client->pos.y, 1);
    packet_send(client, "Current level: %d\n", client->level);
    decreaseResourcesOnMap(server, &client->pos, incantation);
    if (client->level == 8)
        return on_game_win(server);
    return 1;
}

char    onPostIncantPacket(t_server *server,
                                t_client *client,
                                char *packet)
{
    if (!checkIncantationPacket(server, client, packet)) {
        send_gui_packet(server, "pie %d %d %d\n",
                        client->pos.x, client->pos.y, 0);
        return packet_send(client, "ko\n");
    }
    return onLevelUp(server, client);
}
