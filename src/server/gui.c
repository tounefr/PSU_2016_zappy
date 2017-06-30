/*
** gui.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Mon Jun 26 11:53:36 2017 Thomas HENON
** Last update Mon Jun 26 11:53:37 2017 Thomas HENON
*/

#define _GNU_SOURCE
#include <stdio.h>
#include "server.h"

char gui_send_map_case(t_server *server, int x, int y)
{
    int pos;

    pos = x + y * server->map.width;
    send_gui_packet(server, "bct %d %d %d %d %d %d %d %d %d\n",
                    x, y,
                    server->map.cases[pos][TYPE_FOOD],
                    server->map.cases[pos][TYPE_LINEMATE],
                    server->map.cases[pos][TYPE_DERAUMERE],
                    server->map.cases[pos][TYPE_SIBUR],
                    server->map.cases[pos][TYPE_MENDIANE],
                    server->map.cases[pos][TYPE_PHIRAS],
                    server->map.cases[pos][TYPE_THYSTAME]
    );
    return 1;
}

char gui_send_map_content(t_server *server)
{
    int y;
    int x;

    for (y = 0; y < server->map.height; y++) {
        for (x = 0; x < server->map.width; x++) {
            gui_send_map_case(server, x, y);
        }
    }
    return 1;
}

char gui_send_teams(t_server *server)
{
    int i;

    for (i = 0; i < MAX_TEAMS; i++) {
        if (strlen(server->teams[i].name) == 0)
            continue;
        send_gui_packet(server, "tna %s\n", server->teams[i].name);
    }
    return 1;
}

char send_gui_packet(t_server *server, char *format, ...)
{
    va_list args;
    char *buffer;
    t_client *client;

    if (!server->gui_client)
        return 0;
    client = server->gui_client;
    va_start(args, format);
    if (vasprintf(&buffer, format, args) == -1) {
        va_end(args);
        return exit_error(0, "malloc error\n");
    }
    va_end(args);
    if (!generic_list_append(&client->write_packets, buffer))
        return exit_error(0, "malloc error\n");
    return 1;
}

char send_gui_players_connected(t_server *server)
{
    int i;
    t_client *client;

    for (i = 0 ; i < MAX_CLIENTS; i++) {
        client = &server->clients[i];
        if (client->is_gui || client->socket_fd == -1)
            continue;
        send_gui_packet(server, "pnw %d %d %d %d %d %s\n",
                        client->num, client->pos.x,
                        client->pos.y, client->orientation,
                        client->level, client->team->name);
    }
    return 1;
}