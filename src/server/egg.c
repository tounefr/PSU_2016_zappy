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

void init_egg(t_egg *egg)
{

}

char egg_pending_client(t_server *server, t_client *client)
{
    int i;
    t_egg *egg;

    for (i = 0; i < MAX_EGGS; i++) {
        egg = &server->eggs[i];
        if (!egg->pending_client || !egg->master || !egg->master->team)
            continue;
        if (egg->master->team != client->team)
            continue;
        egg->pending_client = 0;
        init_egg(egg);
        printf("connected across a egg\n");
        return 1;
    }
    return 0;
}

char lay_egg(t_server *server, t_client *client)
{
    int i;
    t_egg *egg;
    int p;

    for (i = 0; i < MAX_EGGS; i++) {
        egg = &server->eggs[i];
        if (egg->remain_cycles != 0)
            continue;
        egg->pos = client->pos;
        egg->num = i;
        egg->pending_client = 0;
        egg->remain_cycles = TIME_EGG_HATCHING;
        egg->master = client;
        p = egg->pos.x + egg->pos.y * server->map.height;
        server->map.cases[p][TYPE_EGG]++;
        printf("oeuf pondu\n");
        send_gui_packet(server, "enw %d %d %d %d\n",
                        egg->num, client->num,
                        egg->pos.x, egg->pos.y);
        return 1;
    }
    return exit_error(0, "no egg slot available\n");
}

char hatch_eggs(t_server *server, t_client *client)
{
    int i;
    t_egg *egg;

    for (i = 0; i < MAX_EGGS; i++) {
        egg = &server->eggs[i];
        if ((egg->remain_cycles - 1) == 0) {
            printf("eclosion!!!!!\n");
            egg->pending_client = 1;
            send_gui_packet(server, "eht %d\n", egg->num);
        }
        if (egg->remain_cycles > 0)
            egg->remain_cycles--;
    }
    return 1;
}
