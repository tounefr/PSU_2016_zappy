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
    client_pos = client->pos.x + client->pos.y * server->map.height;
    for (i = 0; i < RESOURCES_NBR_TYPES; i++) {
        if (!is_stone(i) && strcmp((char*)&food, "food"))
            continue;
        if (!strcmp(g_foods[i].s, (char*)&food)) {
            if (client->inventory[g_foods[i].type] - 1 < 0)
                return packet_send(client->socket_fd, "ko\n");
            client->inventory[g_foods[i].type]--;
            server->map.cases[client_pos][g_foods[i].type]++;
            send_gui_packet(server, "pdr %d %d\n",
                            client->num, g_foods[i].type);
            if (g_foods[i].type == TYPE_FOOD)
                client->life_cycles -= CYCLES_PER_LIFE_UNIT;
            return packet_send(client->socket_fd, "ok\n");
        }
    }
    return packet_send(client->socket_fd, "ko\n");
}

char    onTakeObjectPacket(t_server *server, t_client *client, char *packet)
{
    int i;
    char food[100];
    int client_pos;

    memset(&food, 0, sizeof(food));
    strncpy((char*)&food, packet + 5, sizeof(food) - 1);
    client_pos = client->pos.x + client->pos.y * server->map.height;
    for (i = 0; i < RESOURCES_NBR_TYPES; i++) {
        if (!is_stone(i) && strcmp((char*)&food, "food"))
            continue;
        if (!strcmp(g_foods[i].s, (char*)&food)) {
            if (server->map.cases[client_pos][g_foods[i].type] - 1 < 0)
                return packet_send(client->socket_fd, "ko\n");
            client->inventory[g_foods[i].type]++;
            server->map.cases[client_pos][g_foods[i].type]--;
            send_gui_packet(server, "pgt %d %d\n",
                            client->num, g_foods[i].type);
            if (g_foods[i].type == TYPE_FOOD)
                client->life_cycles += CYCLES_PER_LIFE_UNIT;
            return packet_send(client->socket_fd, "ok\n");
        }
    }
    return packet_send(client->socket_fd, "ko\n");
}

char    onEjectPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)client;
    (void)packet;
    return 1;
}

char    onForkPacket(t_server *server, t_client *client, char *packet)
{
    (void)packet;
    if (!init_egg(server, client))
        return packet_send(client->socket_fd, "ko\n");
    return packet_send(client->socket_fd, "ok\n");
}
