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

t_network_commands network_commands[N_NETWORK_COMMANDS] =
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
    { "Take object", onTakeObjectPacket, 7, FLAG_NONE },
    { "Set object", onSetObjectPacket, 7, FLAG_NONE },
    { "Incantation", onIncantationPacket, 300, FLAG_NONE }
};

char    onIncantationPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)client;
    (void)packet;
    return 1;
}

char    onSetObjectPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)client;
    (void)packet;
    return 1;
}

char    onTakeObjectPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)client;
    (void)packet;
    return 1;
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
