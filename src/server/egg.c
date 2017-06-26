
#include "server.h"

char init_egg(t_server *server, t_client *client)
{
    int i;
    t_egg *egg;

    for (i = 0; i < MAX_EGGS_PER_CLIENT; i++) {
        egg = &client->eggs[i];
        if (egg->remain_cycles != 0)
            continue;
        egg->pos = get_random_map_pos(server);
        server->map.cases[egg->pos][TYPE_EGG]++;
        egg->remain_cycles = TIME_EGG_HATCHING;
        return 1;
    }
    return exit_error(0, "no egg slot available\n");
}

char hatch_eggs(t_server *server, t_client *client)
{
    int i;

    (void)server;
    for (i = 0; i < MAX_EGGS_PER_CLIENT; i++) {
        if ((client->eggs[i].remain_cycles - 1) == 0) {
            printf("eclosion!!!!!\n");
        }
        if (client->eggs[i].remain_cycles > 0)
            client->eggs[i].remain_cycles--;
    }
    return 1;
}