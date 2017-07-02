/*
** callback.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 30 21:50:39 2017 Thomas HENON
** Last update Fri Jun 30 21:50:39 2017 Thomas HENON
*/

#include "server.h"

char free_callback(void *data)
{
    t_callback *callback;

    callback = (t_callback*)data;
    free(callback->packet);
    free(callback);
    return 1;
}

t_callback *get_callback(t_client *client,
                         char (*func)(t_server*, t_client*, char*))
{
    t_generic_list *node;
    t_callback *callback;

    node = client->callbacks;
    while (node)
    {
        callback = node->data;
        if (callback->func == func)
            return callback;
        node = node->next;
    }
    return NULL;
}

char add_callback(t_client *client,
                  char (*func)(t_server*, t_client*, char*),
                  int cycles,
                  void *packet)
{
    t_callback *callback;

    if (!(callback = malloc(sizeof(t_callback))))
        return exit_error(0, "malloc error\n");
    callback->packet = packet;
    callback->cycles = cycles;
    callback->func = func;
    if (!generic_list_append(&client->callbacks, callback))
        return 0;
    return 1;
}