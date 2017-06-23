
#include "server.h"
#include "network.h"

char    onLeftPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)client;
    (void)packet;
    return 1;
}

char    onLookPacket(t_server *server, t_client *client, char *packet)
{
    (void)server;
    (void)client;
    (void)packet;
    return 1;
}

char on_welcome(t_server *server, t_client *client, char *packet) {
    int team_i;
    int client_in_team_left;

    if (!strcmp(packet, "GRAPHIC"))
        client->is_gui = 1;
    else {
        if ((team_i = get_team_name_index(server, packet)) == -1)
            return exit_error(0, "can't allocate new team\n");
        client->team_i = team_i;
        client_in_team_left = server->clients_per_team -
                              clients_in_team((t_client*)&server->clients, team_i);
        return dprintf(client->socket_fd, "%d\n", client_in_team_left);
    }
    return 1;
}