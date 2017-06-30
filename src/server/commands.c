/*
** commands.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Fri Jun 23 15:00:43 2017 Thomas HENON
** Last update Tue Jun 27 11:26:56 2017 arsene
*/

#include "server.h"

char    onSetObjectPacket(t_server *server, t_client *client, char *packet)
{
    int i;
    char food[100];
    int client_pos;

    memset((char*)&food, 0, sizeof(food));
    strncpy((char*)&food, packet + 5, sizeof(food) - 1);
    client_pos = client->pos.x + client->pos.y * server->map.width;
    for (i = 0; i < RESOURCES_NBR_TYPES; i++) {
        if (!is_stone(i) && strcmp((char*)&food, "food"))
            continue;
        if (!strcmp(get_g_foods()[i].s, (char*)&food)) {
            if (client->inventory[get_g_foods()[i].type] - 1 < 0)
                return packet_send(client, "ko\n");
            client->inventory[get_g_foods()[i].type]--;
            server->map.cases[client_pos][get_g_foods()[i].type]++;
            send_gui_packet(server, "pdr %d %d\n",
                            client->num, get_g_foods()[i].type);
            if (get_g_foods()[i].type == TYPE_FOOD)
                client->life_cycles -= CYCLES_PER_LIFE_UNIT;
            gui_send_map_case(server, client->pos.x, client->pos.y);
            return packet_send(client, "ok\n");
        }
    }
    return packet_send(client, "ko\n");
}


char    onTakeObjectPacket(t_server *server, t_client *client, char *packet)
{
    int i;
    char food[100];
    int client_pos;

    memset(&food, 0, sizeof(food));
    strncpy((char*)&food, packet + 5, sizeof(food) - 1);
    client_pos = client->pos.x + client->pos.y * server->map.width;
    for (i = 0; i < RESOURCES_NBR_TYPES; i++) {
        if (!is_stone(i) && strcmp((char*)&food, "food"))
            continue;
        if (!strcmp(get_g_foods()[i].s, (char*)&food)) {
            if (server->map.cases[client_pos][get_g_foods()[i].type] - 1 < 0)
                return packet_send(client, "ko\n");
            client->inventory[get_g_foods()[i].type]++;
            server->map.cases[client_pos][get_g_foods()[i].type]--;
            send_gui_packet(server, "pgt %d %d\n",
                            client->num, get_g_foods()[i].type);
            if (get_g_foods()[i].type == TYPE_FOOD)
                client->life_cycles += CYCLES_PER_LIFE_UNIT;
            gui_send_map_case(server, client->pos.x, client->pos.y);
            return packet_send(client, "ok\n");
        }
    }
    return packet_send(client, "ko\n");
}

char    onPreForkPacket(t_server *server, t_client *client, char *packet)
{
    (void)packet;
    send_gui_packet(server, "pfk %d\n", client->num);
    return 1;
}

char    onPostForkPacket(t_server *server, t_client *client, char *packet)
{
    (void)packet;
    if (!lay_egg(server, client))
        return packet_send(client, "ko\n");
    return packet_send(client, "ok\n");
}
