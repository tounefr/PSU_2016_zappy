/*
** util2.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sun Jul  2 20:04:23 2017 Thomas HENON
** Last update Sun Jul  2 20:04:23 2017 Thomas HENON
*/

#include "server.h"

void free_null(void **data)
{
    if (*data)
        free(*data);
    *data = NULL;
}