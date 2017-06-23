
#include <string.h>
#include <stdlib.h>
#include "server.h"
#include "network.h"

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
