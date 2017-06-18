/*
** generic_list.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_myirc
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sun Jun  4 12:01:59 2017 Thomas HENON
** Last update Sun Jun  4 12:01:59 2017 Thomas HENON
*/

#include "generic_list.h"

static char
generic_list_new(t_generic_list **list,
                 void *data)
{
    *list = my_malloc(sizeof(t_generic_list));
    (*list)->data = data;
    (*list)->prev = NULL;
    (*list)->next = NULL;
    return 1;
}

char
generic_list_free(t_generic_list **elem,
                  char (*callback_free_elem)(void *data))
{
    (void)elem;
    (void)callback_free_elem;
    return 1;
}

char
generic_list_append(t_generic_list **list,
                    void *elem)
{
    t_generic_list *cur;

    if (*list == NULL)
        return generic_list_new(list, elem);
    cur = *list;
    while (cur->next)
        cur = cur->next;
    return generic_list_new(&cur->next, elem);
}

char
generic_list_prepend(t_generic_list **list,
                     void *elem)
{
    t_generic_list *save;

    save = *list;
    if (!(generic_list_new(list, elem)))
        return 0;
    (*list)->next = save;
    return 1;
}

char
generic_list_remove(t_generic_list **list,
                    void *elem,
                    char (*rm_func)(void *))
{
    t_generic_list *cur;
    t_generic_list *prev;

    if (!list || !*list)
        return 0;
    cur = *list;
    prev = NULL;
    while (cur) {
        if (cur->data == elem) {
            if (prev)
                prev->next = cur->next;
            else if (cur->next)
                *list = cur->next;
            else
                *list = NULL;
            if (rm_func)
                return rm_func(elem);
            return 1;
        }
        prev = cur;
        cur = cur->next;
    }
    return 0;
}
