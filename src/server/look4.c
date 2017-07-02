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

void convertView2(t_look *see, int *index, char **buffer)
{
    int first;
    int i;
    int x;

    if (*index != 0)
        *buffer = myAppend(*buffer, ",");
    i = 0;
    first = 1;
    for (i = 0; i < 9; i++) {
        x = 0;
        while (x < see->cell[*index].content[i])
        {
            if (first != 1)
                *buffer = myAppend(*buffer, " ");
            first = 0;
            *buffer = myAppend(*buffer, get_type(i));
            x++;
        }
    }
    (*index)++;
}

void	convertView(t_client *c, t_look *see)
{
    char	*buffer;
    int	limit;
    int	index;
    int	i;

    i = -1;
    limit = 1;
    while (++i < c->level)
        limit += limit + 2;
    index = 0;
    if ((buffer = malloc(1)) == NULL)
        return;
    buffer[0] = 0;
    buffer = myAppend(buffer, "[");
    while (index < limit) {
        convertView2(see, &index, &buffer);
    }
    buffer = myAppend(buffer, "]");
    packet_send(c, "%s\n", buffer);
    free(buffer);
}
