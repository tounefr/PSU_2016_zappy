/*
** resources.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Sat Jun 24 16:09:57 2017 Thomas HENON
** Last update Sun Jul  2 17:05:21 2017 arsene
*/

#include <stdio.h>
#include <time.h>
#include "server.h"

char is_stone(int type) {
    return (type == TYPE_LINEMATE || type == TYPE_DERAUMERE ||
            type == TYPE_SIBUR || type == TYPE_MENDIANE ||
            type == TYPE_MENDIANE || type == TYPE_PHIRAS ||
            type == TYPE_THYSTAME);
}

void take_ressource(t_server *server, int client_pos, int i) {
    int x;
    int y;
    int pos;

    server->map.cases[client_pos][get_g_foods()[i].type]--;
    x = my_rand(0, server->map.width - 1);
    y = my_rand(0, server->map.height - 1);
    pos = x + (y * server->map.height);
    server->map.cases[pos][get_g_foods()[i].type]++;
}

void rand_ressource(t_server *server, int p) {
    int item;

    item = (rand() % (100 - 0) + 0);
    if (item <= 54)
        return;
    else if (item <= 55 && item > 54)
        server->map.cases[p][TYPE_THYSTAME]++;
    else if (item <= 57 && item > 55)
        server->map.cases[p][TYPE_MENDIANE]++;
    else if (item <= 59 && item > 57)
        server->map.cases[p][TYPE_PHIRAS]++;
    else if (item <= 62 && item > 59)
        server->map.cases[p][TYPE_SIBUR]++;
    else if (item <= 65 && item > 62)
        server->map.cases[p][TYPE_DERAUMERE]++;
    else if (item <= 75 && item > 65)
        server->map.cases[p][TYPE_LINEMATE]++;
    else if (item <= 100 && item > 75)
        server->map.cases[p][TYPE_FOOD]++;
}

char generate_resources(t_server *server) {
    int x;
    int y;
    int p;

    printf("MAP: %i x %i\n", server->map.width, server->map.height);
    for (y = 0; y < server->map.height; y++) {
        for (x = 0; x < server->map.width; x++) {
            p = y * server->map.width + x;
            rand_ressource(server, p);
        }
    }
    printf("resources generated\n");
    gui_send_map_content(server);
    return 1;
}
