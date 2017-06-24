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
#include "network.h"

t_network_commands network_commands[N_NETWORK_COMMANDS] =
{
    { "Forward", onForwardPacket, FLAG_NONE },
    { "Right", onRightPacket, FLAG_NONE },
    { "Left", onLeftPacket, FLAG_NONE },
    { "Look", onLookPacket, FLAG_NONE },
    { "Inventory", onInventoryPacket, FLAG_NONE },
    { "Broadcast", onBroadcastPacket, FLAG_NONE },
    { "Connect_nbr", onConnectNbrPacket, FLAG_NONE },
    { "Fork", onForkPacket, FLAG_NONE },
    { "Eject", onEjectPacket, FLAG_NONE },
    { "Take object", onTakeObjectPacket, FLAG_NONE },
    { "Set object", onSetObjectPacket, FLAG_NONE },
    { "Incantation", onIncantationPacket, FLAG_NONE }
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
