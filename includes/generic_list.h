/*
** generic_list.h for  in /home/toune/Documents/Epitech/projets/PSU_2016_myirc
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sun Jun  4 12:04:27 2017 Thomas HENON
** Last update Sun Jun  4 12:04:27 2017 Thomas HENON
*/

#ifndef PROJETS_GENERIC_LIST_H
#define PROJETS_GENERIC_LIST_H

#include "util.h"

typedef struct s_generic_list
{
    void *data;
    struct s_generic_list *prev;
    struct s_generic_list *next;
} t_generic_list;

char
generic_list_free(t_generic_list **list,
                  char (*callback_free_elem)(void *data));
char
generic_list_append(t_generic_list **list,
                    void *elem);
char
generic_list_prepend(t_generic_list **list,
                     void *elem);
char
generic_list_remove(t_generic_list **list,
                    void *elem,
                    char (*rm_func)(void *));
void*
generic_list_foreach(t_generic_list *list);
void*
generic_list_get_at(t_generic_list *list,
                    int i);
int
generic_list_count(t_generic_list *list);

void
generic_list_destory(t_generic_list **list,
                     char (*rm_func)(void *));

#endif //PROJETS_GENERIC_LIST_H
