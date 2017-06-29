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

char parse_team_names(t_server *server, int *i, int ac, char **av)
{
    int i2;
    int i3;
    t_team *team;

    i3 = 0;
    for (i2 = *i + 1; i2 < ac && av[i2][0] != '-'; i2++) {
        if (!strcasecmp("GRAPHICAL", av[i2]))
            continue;
        team = &server->teams[i3++];
        strncpy((char *) &team->name, av[i2], TEAM_NAME_MAX_LEN - 1);
        team->slots = server->clients_per_team;
    }
    *i = i2;
    return 1;
}