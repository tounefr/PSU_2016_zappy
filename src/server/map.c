/*
** map.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:00:58 2017 Thomas HENON
** Last update Fri Jun 23 15:00:58 2017 Thomas HENON
*/

#include "server.h"
#include "network.h"

void init_map(t_map *map)
{
    int max_mapsize;
    int i;
    int i2;

    max_mapsize = MAX_MAP_HEIGHT * MAX_MAP_HEIGHT;
    map->width = DEFAULT_MAP_SIZE;
    map->height = DEFAULT_MAP_SIZE;
    for (i = 0; i < max_mapsize; i++) {
        for (i2 = 0; i2 < RESOURCES_NBR_TYPES; i2++)
            map->cases[i][i2] = 0;
    }
}
