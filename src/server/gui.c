/*
** gui.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Mon Jun 26 11:53:36 2017 Thomas HENON
** Last update Mon Jun 26 11:53:37 2017 Thomas HENON
*/

#include <stdio.h>
#include "server.h"

char gui_send_map_content(t_server *server, t_client *client)
{
    int y;
    int x;
    int pos;

    for (y = 0; y < server->map.height; y++) {
        for (x = 0; x < server->map.width; x++) {
            pos = x + y * server->map.height;
            dprintf(client->socket_fd, "bct %d %d %d %d %d %d %d %d %d\n",
                    x, y,
                    server->map.cases[pos][TYPE_FOOD],
                    server->map.cases[pos][TYPE_LINEMATE],
                    server->map.cases[pos][TYPE_DERAUMERE],
                    server->map.cases[pos][TYPE_SIBUR],
                    server->map.cases[pos][TYPE_MENDIANE],
                    server->map.cases[pos][TYPE_PHIRAS],
                    server->map.cases[pos][TYPE_THYSTAME]
            );
        }
    }
    return 1;
}

char gui_send_teams(t_server *server, t_client *client)
{
    int i;

    for (i = 0; i < MAX_TEAMS; i++) {
        if (strlen(server->teams[i].name) == 0)
            continue;
        packet_send(client->socket_fd, "tna %s\n", server->teams[i].name);
    }
    return 1;
}

char send_gui_packet(t_server *server, char *packet, ...)
{
    va_list args;

    va_start(args, packet);
    if (!server->gui_client)
        return exit_error(0, "no gui client connected\n");
    vdprintf(server->gui_client->socket_fd, packet, args);
    va_end(args);
    return 1;
}
