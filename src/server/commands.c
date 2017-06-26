/*
** commands.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:00:43 2017 Thomas HENON
** Last update Fri Jun 23 15:00:44 2017 Thomas HENON
*/

#include "server.h"

t_network_commands g_network_commands[N_NETWORK_COMMANDS] =
{
    { "Forward", onForwardPacket, 7, FLAG_NONE },
    { "Right", onRightPacket, 7, FLAG_NONE },
    { "Left", onLeftPacket, 7, FLAG_NONE },
    { "Look", onLookPacket, 7, FLAG_NONE },
    { "Inventory", onInventoryPacket, 1, FLAG_NONE },
    { "Broadcast", onBroadcastPacket, 7, FLAG_NONE },
    { "Connect_nbr", onConnectNbrPacket, 0, FLAG_NONE },
    { "Fork", onForkPacket, 42, FLAG_NONE },
    { "Eject", onEjectPacket, 7, FLAG_NONE },
    { "Take", onTakeObjectPacket, 7, FLAG_NONE },
    { "Set", onSetObjectPacket, 7, FLAG_NONE },
    { "Incantation", onIncantationPacket, 300, FLAG_NONE }
};

t_incantation g_incantations[NBR_LEVELS] =
{
        { 1, { 0, 1, 0, 0, 0, 0, 0 } },
        { 2, { 0, 1, 1, 1, 0, 0, 0 } },
        { 2, { 0, 2, 0, 1, 0, 2, 0 } },
        { 4, { 0, 1, 1, 2, 0, 1, 0 } },
        { 4, { 0, 1, 2, 1, 3, 0, 0 } },
        { 6, { 0, 1, 2, 3, 0, 1, 0 } },
        { 6, { 0, 2, 2, 2, 2, 2, 1 } }
};

t_food g_foods[RESOURCES_NBR_TYPES] =
{
        { "food", TYPE_FOOD },
        { "thystame", TYPE_THYSTAME },
        { "phiras", TYPE_PHIRAS },
        { "mendiane", TYPE_MENDIANE },
        { "sibur", TYPE_SIBUR },
        { "deraumere", TYPE_DERAUMERE },
        { "linemate", TYPE_LINEMATE },
        { "player", TYPE_PLAYER }
};

char    onIncantationPacket(t_server *server, t_client *client, char *packet)
{
    int i;
    t_incantation *incantation;

    if (client->level > 7)
        return packet_send(client->socket_fd, "ko\n");
    incantation = &g_incantations[client->level - 1];
    int i2 = client->pos.x + client->pos.y * server->map.height;
    for (i = 0; i < RESOURCES_NBR_TYPES; i++) {
        if (server->map.cases[i2][i] != client->inventory[i]) {
            printf("not enough ressources\n");
            return packet_send(client->socket_fd, "ko\n");
        }
    }
    if (client->level + 1 > MAX_LEVEL)
        return packet_send(client->socket_fd, "ko\n");
    client->level++;
    packet_send(client->socket_fd, "Current level: %d\n", client->level);
    return 1;
}

char    onSetObjectPacket(t_server *server, t_client *client, char *packet)
{
    int i;
    char food[100];
    int client_pos;

    memset((char*)&food, 0, sizeof(food));
    strncpy((char*)&food, packet + 5, sizeof(food) - 1);
    client_pos = client->pos.x + client->pos.y * server->map.height;
    for (i = 0; i < RESOURCES_NBR_TYPES; i++) {
        if (!strcmp((char*)&food, "player"))
            continue;
        if (!strcmp(g_foods[i].s, (char*)&food)) {
            if (client->inventory[g_foods[i].type] - 1 < 0)
                return packet_send(client->socket_fd, "ko\n");
            client->inventory[g_foods[i].type]--;
            server->map.cases[client_pos][g_foods[i].type]++;
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
        if (!strcmp((char*)&food, "player"))
            continue;
        if (!strcmp(g_foods[i].s, (char*)&food)) {
            if (server->map.cases[client_pos][g_foods[i].type] - 1 < 0)
                return packet_send(client->socket_fd, "ko\n");
            client->inventory[g_foods[i].type]++;
            server->map.cases[client_pos][g_foods[i].type]--;
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
    (void)server;
    (void)packet;
    packet_send(client->socket_fd, "ok\n");
    return 1;
}
