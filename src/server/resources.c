/*
** resources.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Sat Jun 24 16:09:57 2017 Thomas HENON
** Last update Fri Jun 30 10:36:44 2017 Didier
*/

#include <stdio.h>
#include <time.h>
#include "server.h"

char is_stone(int type)
{
    return (type == TYPE_LINEMATE || type == TYPE_DERAUMERE ||
            type == TYPE_SIBUR || type == TYPE_MENDIANE ||
            type == TYPE_MENDIANE || type == TYPE_PHIRAS ||
            type == TYPE_THYSTAME);
}

void	rand_ressource(t_server *server, int p)
{
  int	item;

  item = (rand() % (100 - 0) + 0);
  if (item <= 60)
    return;
  else if (item <= 61 && item > 60)
    server->map.cases[p][TYPE_THYSTAME]++;
  else if (item <= 63 && item > 61)
    server->map.cases[p][TYPE_MENDIANE]++;
  else if (item <= 66 && item > 63)
    server->map.cases[p][TYPE_PHIRAS]++;
  else if (item <= 69 && item > 66)
    server->map.cases[p][TYPE_SIBUR]++;
  else if (item <= 71 && item > 69)
    server->map.cases[p][TYPE_DERAUMERE]++;
  else if (item <= 81 && item > 71)
    server->map.cases[p][TYPE_LINEMATE]++;
  else if (item <= 100 && item > 81)
    server->map.cases[p][TYPE_FOOD]++;
}

char	generate_resources(t_server *server)
{
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
