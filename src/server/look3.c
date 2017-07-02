/*
** look3.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sun Jul  2 20:59:32 2017 Thomas HENON
** Last update Sun Jul  2 20:59:33 2017 Thomas HENON
*/

#include <stdlib.h>
#include <string.h>
#include "server.h"

void    lookLeft(t_server *s, t_client *c, t_look *see)
{
    t_pos target;
    t_pos tmp;
    int   range;
    int   index;

    range = 0;
    index = 0;
    target = c->pos;
    while (range < 8)
    {
        tmp = target;
        tmp.y += range;
        while (tmp.y >= target.y - range)
        {
            get_ressources(s, see, index, coordsToIndex(s, tmp));
            tmp.y--;
            index++;
        }
        target.x--;
        range++;
    }
}

void    lookRight(t_server *s, t_client *c, t_look *see)
{
    t_pos target;
    t_pos tmp;
    int   range;
    int   index;

    range = 0;
    index = 0;
    target = c->pos;
    while (range < 8)
    {
        tmp = target;
        tmp.y -= range;
        while (tmp.y <= target.y + range)
        {
            get_ressources(s, see, index, coordsToIndex(s, tmp));
            tmp.y++;
            index++;
        }
        target.x++;
        range++;
    }
}

char		*get_type(int i)
{
    if (i == TYPE_FOOD)
        return ("food");
    else if (i == TYPE_LINEMATE)
        return ("linemate");
    else if (i == TYPE_DERAUMERE)
        return ("deraumere");
    else if (i == TYPE_SIBUR)
        return ("sibur");
    else if (i == TYPE_MENDIANE)
        return ("mendiane");
    else if (i == TYPE_PHIRAS)
        return ("phiras");
    else if (i == TYPE_THYSTAME)
        return ("thystame");
    else if (i == TYPE_PLAYER)
        return ("player");
    else if (i == TYPE_EGG)
        return ("egg");
    return "";
}

char	*myAppend(char *old, char *str)
{
    char	*new;
    int	size;

    new = NULL;
    size = strlen(old) + strlen(str);
    if ((new = malloc((size + 1) * sizeof(char))) == NULL)
        return (new);
    new[0] = '\0';
    strcat(new, old);
    strcat(new, str);
    new[size] = '\0';
    if (old != NULL)
        free(old);
    return (new);
}