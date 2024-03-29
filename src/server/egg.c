/*
** egg.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Mon Jun 26 15:17:40 2017 Thomas HENON
** Last update Mon Jun 26 15:17:40 2017 Thomas HENON
*/

#include "server.h"

char lay_egg(t_server *server, t_client *client)
{
    static int egg_num = 0;
    t_egg *egg;
    int p;

    if (!(egg = malloc(sizeof(t_egg))))
        return exit_error(0, "malloc error\n");
    if (!generic_list_append(&client->eggs, egg))
        return 0;
    egg->pos = client->pos;
    egg->num = egg_num++;
    egg->pending_client = 0;
    p = egg->pos.x + egg->pos.y * server->map.width;
    server->map.cases[p][TYPE_EGG]++;
    printf("egg layed\n");
    if (!add_callback(client, hatch_egg, 600, (void*)egg))
        return 0;
    send_gui_packet(server, "enw %d %d %d %d\n",
                    egg->num, client->num,
                    egg->pos.x, egg->pos.y);
    return 1;
}

char hatch_egg(t_server *server, t_client *client, char *packet)
{
    t_egg *egg;

    egg = (t_egg*)packet;
    if (egg) {
        egg->pending_client = 1;
        send_gui_packet(server, "eht %d\n", egg->num);
    }
    client->team->slots++;
    printf("hatch egg\n");
    return 1;
}

char remove_hatched_egg(t_server *server, t_client *join_client)
{
    t_generic_list *node;
    t_egg *egg;
    t_client *client;
    int i;

    for (i = 0; i < MAX_CLIENTS; i++) {
        client = &server->clients[i];
        if (client->socket_fd == -1 || client->is_gui ||
            client->team != join_client->team)
            continue;
        node = client->eggs;
        while (node) {
            egg = node->data;
            if (egg->pending_client) {
                join_client->pos = client->pos;
                generic_list_remove(&client->eggs, egg, default_free);
                printf("USING EGG SLOT\n");
                send_gui_packet(server, "ebo %d\n", egg->num);
                return 1;
            }
            node = node->next;
        }
    }
    return 0;
}