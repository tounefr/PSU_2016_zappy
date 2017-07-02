/*
** resources.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Sat Jun 24 16:09:57 2017 Thomas HENON
** Last update Sun Jul  2 19:14:54 2017 arsene
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
    gui_send_map_case(server, client_pos % server->map.height,
                      client_pos / server->map.height);
    x = my_rand(0, server->map.width - 1);
    y = my_rand(0, server->map.height - 1);
    pos = x + (y * server->map.height);
    server->map.cases[pos][get_g_foods()[i].type]++;
    gui_send_map_case(server, pos % server->map.height,
                      pos / server->map.height);
}

void rand_ressource(t_server *server, int p) {
  int item;

  item = (rand() % (100 - 0) + 0);
  if (item <= 20)
    return;
  if (item <= 35  && item > 20)
    server->map.cases[p][TYPE_THYSTAME]++;
  if (item <= 45 && item > 25)
    server->map.cases[p][TYPE_MENDIANE]++;
  if (item <= 55 && item > 30)
    server->map.cases[p][TYPE_PHIRAS]++;
  if (item <= 65 && item > 45)
    server->map.cases[p][TYPE_SIBUR]++;
  if (item <= 70 && item > 50)
    server->map.cases[p][TYPE_DERAUMERE]++;
  if (item <= 95 && item > 65)
    server->map.cases[p][TYPE_LINEMATE]++;
  if (item <= 100 && item > 30)
    server->map.cases[p][TYPE_FOOD]++;
  if (item <= 100 && item > 60)
    server->map.cases[p][TYPE_FOOD] = server->map.cases[p][TYPE_FOOD] + 2;
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
