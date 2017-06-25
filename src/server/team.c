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

int get_team_name_index(t_server *server, char *team_name)
{
    int i;
    char *unused_team_name;
    int unused_team_name_i;

    unused_team_name = NULL;
    for (i = 0; i < MAX_TEAMS; i++) {
        if (!strcmp(server->teams_name[i], team_name))
            return i;
        else if (server->teams_name[i][0] == 0) {
            unused_team_name = (char*)&server->teams_name[i];
            unused_team_name_i = i;
        }
    }
    if (unused_team_name) {
        strncpy(unused_team_name, team_name, TEAM_NAME_MAX_LEN);
        return unused_team_name_i;
    }
    return -1;
}
