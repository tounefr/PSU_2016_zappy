/*
** commands3.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:00:53 2017 Thomas HENON
** Last update Fri Jun 23 15:00:54 2017 Thomas HENON
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
    packet_send(client->socket_fd, "ok\n");
    return 1;
}

char    onLookPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)client;
    (void)packet;

    return 1;
}

char on_welcome(t_server *server, t_client *client, char *packet)
{
    int team_i;
    int client_in_team_left;

    if (!strcmp(packet, "GRAPHIC"))
        client->is_gui = 1;
    else {
        if ((team_i = get_team_name_index(server, packet)) == -1) {
            dprintf(client->socket_fd, "ko\n");
            return exit_error(0, "can't allocate new team\n");
        }
        client->team_i = team_i;
        client_in_team_left = server->clients_per_team -
                              clients_in_team((t_client*)&server->clients, team_i);
        dprintf(client->socket_fd, "%d\n", client_in_team_left);
        dprintf(client->socket_fd, "%d %d\n", server->map.width, server->map.height);
        return 1;
    }
    return 1;
}
