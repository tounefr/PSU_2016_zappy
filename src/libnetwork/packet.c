/*
** packet.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sun Jul  2 19:50:38 2017 Thomas HENON
** Last update Sun Jul  2 19:50:39 2017 Thomas HENON
*/

#include <stdlib.h>
#include <stdio.h>

char *recv_packet(int fd)
{
    static size_t n = 0;
    static char *buffer = NULL;
    static FILE *stream = NULL;

    if (!buffer) {
        if (!(stream = fdopen(fd, "r+")))
            return NULL;
        if (setvbuf(stream, NULL, _IOLBF, 0) != 0)
            return NULL;
        buffer = NULL;
    }
    if (-1 == getline(&buffer, &n, stream))
        return NULL;
    return buffer;
}
