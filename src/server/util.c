/*
** util.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:01:31 2017 Thomas HENON
** Last update Fri Jun 23 15:01:31 2017 Thomas HENON
*/

#include <stdlib.h>
#include <string.h>
#include "server.h"

char is_legal_network_char(char c)
{
    return (!(c >= 32 && c <= 126) &&
            c != '\n');
}

char is_numeric(char *s)
{
    int len;
    int i;

    len = strlen(s);
    if (len == 0)
        return 0;
    for (i = 0; i < len; i++) {
        if (s[i] < '0' || s[i] > '9')
            return 0;
    }
    return 1;
}

int my_rand(int a, int b)
{
    return rand() % (b - a) + a;
}

int get_pos(t_server *server, t_pos *pos)
{
    return pos->y * server->map.width + pos->x;
}