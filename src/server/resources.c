/*
** resources.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sat Jun 24 16:09:57 2017 Thomas HENON
** Last update Sat Jun 24 16:09:57 2017 Thomas HENON
*/

#include <stdio.h>
#include "server.h"

char is_stone(int type)
{
    return (type == TYPE_LINEMATE || type == TYPE_DERAUMERE ||
            type == TYPE_SIBUR || type == TYPE_MENDIANE ||
            type == TYPE_MENDIANE || type == TYPE_PHIRAS ||
            type == TYPE_THYSTAME);
}

char generate_resources(t_server *server)
{
    int x;
    int y;
    int p;


    for (y = 0; y < server->map.height; y++) {
        for (x = 0; x < server->map.width; x++) {
            p = y * server->map.height + x;
            server->map.cases[p][TYPE_LINEMATE]++;
            server->map.cases[p][TYPE_DERAUMERE]++;
            server->map.cases[p][TYPE_SIBUR]++;
            server->map.cases[p][TYPE_MENDIANE]++;
            server->map.cases[p][TYPE_PHIRAS]++;
            server->map.cases[p][TYPE_THYSTAME]++;
            server->map.cases[p][TYPE_FOOD]++;

            // temporaire
            server->map.cases[p][TYPE_LINEMATE] = 100;
            server->map.cases[p][TYPE_DERAUMERE] = 100;
            server->map.cases[p][TYPE_SIBUR] = 100;
            server->map.cases[p][TYPE_MENDIANE] = 100;
            server->map.cases[p][TYPE_PHIRAS] = 100;
            server->map.cases[p][TYPE_THYSTAME] = 100;
            server->map.cases[p][TYPE_FOOD] = 100;
        }
    }
    printf("New ressources generated\n");
    return 1;
}
