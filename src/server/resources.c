/*
** resources.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Sat Jun 24 16:09:57 2017 Thomas HENON
** Last update Mon Jun 26 12:02:49 2017 arsene
*/

#include <stdio.h>
#include <time.h>
#include "server.h"

void	rand_ressource(t_server *server, int p)
{
  int	item;

  item = (rand() % (b - a) + a);
  if (item <= 56)
    break;
  else if (item <= 57 && item > 56)
    server->map.cases[p][TYPE_THYSTAME]++;
  else if (item <= 61 && item > 57)
    server->map.cases[p][TYPE_MENDIANE]++;
  else if (item <= 66 && item > 61)
    server->map.cases[p][TYPE_PHIRAS]++;
  else if (item <= 73 && item > 66)
    server->map.cases[p][TYPE_SIBUR]++;
  else if (item <= 80 && item > 73)
    server->map.cases[p][TYPE_DERAUMERE]++;
  else if (item <= 90 && item > 80)
    server->map.cases[p][TYPE_LINEMATE]++;
  else if (item <= 100 && item > 90)
    server->map.cases[p][TYPE_FOOD]++;
}

char	generate_resources(t_server *server)
{
    int x;
    int y;
    int p;

    srand(time(NULL));
    for (y = 0; y < server->map.height; y++) {
        for (x = 0; x < server->map.width; x++) {
            p = y * server->map.height + x;
	    rand_ressource(server, p);
        }
    }
    return 1;
}
