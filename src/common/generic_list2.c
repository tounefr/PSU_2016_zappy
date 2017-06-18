/*
** generic_list2.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_myirc
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sun Jun  4 12:02:04 2017 Thomas HENON
** Last update Sun Jun  4 12:02:04 2017 Thomas HENON
*/

#include <stdlib.h>
#include "generic_list.h"

void*
generic_list_foreach(t_generic_list *list)
{
    static t_generic_list *save = NULL;
    t_generic_list *returnv;

    if (!list && !save)
        return NULL;
    if (list)
        save = list;
    returnv = save;
    if (save)
        save = save->next;
    return returnv->data;
}

void*
generic_list_get_at(t_generic_list *list,
                    int i)
{
    (void)list;
    (void)i;
    return NULL;
}

int
generic_list_count(t_generic_list *list)
{
    int c;
    void *elem;

    c = 0;
    while ((elem = generic_list_foreach(list))) {
        list = NULL;
        c++;
    }
    return c;
}

void
generic_list_destory(t_generic_list **list,
                     char (*rm_func)(void *))
{
    void *elem;
    t_generic_list *tmp;

    if (!list || !*list)
        return;
    tmp = *list;
    while ((elem = generic_list_foreach(tmp))) {
        tmp = NULL;
        generic_list_remove(list, elem, rm_func);
    }
    free(*list);
    *list = NULL;
}
