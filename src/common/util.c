/*
** util.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_myirc
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sat May 27 20:17:15 2017 Thomas HENON
** Last update Sat May 27 20:17:15 2017 Thomas HENON
*/

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include "util.h"

char
is_number(char *str)
{
    if (strlen(str) == 0)
        return 0;
    while (*str) {
        if (*str < '0' || *str > '9')
            return 0;
        str++;
    }
    return 1;
}

void
*my_malloc(size_t size)
{
    void    *ptr;

    if (!(ptr = calloc(1, size))) {
        fprintf(stderr, "malloc error\n");
        exit(1);
    }
    return ptr;
}

int
nbr_chars_in_str(char *str,
                 char c)
{
    int i;
    int n;

    n = 0;
    i = -1;
    while (str[++i]) {
        if (str[i] == c)
            n++;
    }
    return n;
}

char
*my_strdup(char *str)
{
    if (!(str = strdup(str)))
        malloc_error();
    return str;
}

char
is_ipv4(char *str)
{
    int i;
    int i2;
    int i3;

    i = -1;
    i2 = 0;
    i3 = 0;
    while (str[++i]) {
        if ((str[i] < '0' || str[i] > '9') && str[i] != '.')
            return 0;
        if (i >= 1 && str[i] == '.' &&
                (str[i - 1] == '.' || str[i + 1] == '.'))
            return 0;
        if (str[i] == '.') {
            i2++;
            i3 = 0;
        }
        if (str[i] >= '0' && str[i] <= '9')
            i3++;
        if (i2 > 3 || i3 > 3)
            return 0;
    }
    return 1;
}