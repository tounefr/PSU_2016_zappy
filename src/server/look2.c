/*
** look2.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sun Jul  2 16:03:21 2017 Thomas HENON
** Last update Sun Jul  2 16:03:22 2017 Thomas HENON
*/

#include "server.h"

int coordsToIndex(t_server *server, t_pos pos) {
    while (pos.x < 0)
        pos.x += server->map.width;
    while (pos.x > server->map.width)
        pos.x -= server->map.width;
    while (pos.y < 0)
        pos.y += server->map.height;
    while (pos.y > server->map.height)
        pos.y -= server->map.height;
    return ((pos.y * server->map.width) + pos.x);
}

void init_look(t_look *tmp)
{
    int i;
    int j;

    i = 0;
    while (i < 64) {
        j = 0;
        while (j < 9) {
            tmp->cell[i].content[j] = 0;
            j++;
        }
        i++;
    }
}

void get_ressources(t_server *s, t_look *see, int index, int pos)
{
    int i;

    i = 0;
    while (i < 9) {
        see->cell[index].content[i] = s->map.cases[pos][i];
        i++;
    }
}

void lookUp(t_server *s, t_client *c, t_look *see)
{
    t_pos target;
    t_pos tmp;
    int range;
    int index;

    range = 0;
    index = 0;
    target = c->pos;
    while (range < 8) {
        tmp = target;
        tmp.x -= range;
        while (tmp.x <= target.x + range) {
            get_ressources(s, see, index, coordsToIndex(s, tmp));
            tmp.x++;
            index++;
        }
        target.y--;
        range++;
    }
}

void lookDown(t_server *s, t_client *c, t_look *see)
{
    t_pos target;
    t_pos tmp;
    int range;
    int index;

    range = 0;
    index = 0;
    target = c->pos;
    while (range < 8) {
        tmp = target;
        tmp.x += range;
        while (tmp.x >= target.x - range) {
            get_ressources(s, see, index, coordsToIndex(s, tmp));
            tmp.x--;
            index++;
        }
        target.y++;
        range++;
    }
}
