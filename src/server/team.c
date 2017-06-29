/*
** team.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:01:05 2017 Thomas HENON
** Last update Fri Jun 23 15:01:06 2017 Thomas HENON
*/

#include <string.h>
#include <stdlib.h>
#include "server.h"

char client_assign_team(t_server *server, t_client *client, char *packet)
{
    int i;
    for (i = 0; i < MAX_TEAMS; i++) {
        if (!strcmp(packet, server->teams[i].name)) {
            client->team = &server->teams[i];
            return 1;
        }
    }
    return exit_error(0, "can't allocat new team\n");
}

int clients_in_team(t_server *server, t_team *team)
{
    int i;
    int c;

    c = 0;
    for (i = 0; i < MAX_CLIENTS; i++) {
        if (server->clients[i].team == team)
            c++;
    }
    return c;
}