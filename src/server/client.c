
#include <stdio.h>
#include <string.h>
#include "server.h"
#include "network.h"

void init_client(t_client *client)
{
    int i;

    client->socket_fd = -1;
    memset(&client->buffer, 0, sizeof(client->buffer));
    client->team_i = -1;
    client->client_num = -1;
    client->pos.x = 0;
    client->pos.y = 0;
    client->packet_i = 0;
    client->is_gui = 0;
    for (i = 0; i < RESOURCES_NBR_TYPES; i++)
        client->inventory[i] = 0;
}

int clients_in_team(t_client *clients, int team_i)
{
    int i;
    int c;

    c = 0;
    for (i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].team_i == team_i)
            c++;
    }
    return c;
}

char on_new_client(t_server *server)
{
    int i;

    i = 0;
    for (i = 0; i < MAX_CLIENTS; i++) {
        if (server->clients[i].socket_fd == -1) {
            printf("new co\n");
            server->clients[i].socket_fd = socket_accept(server->server_fd);
            return socket_send(server->clients[i].socket_fd, "BIENVENUE\n");
        }
    }
    printf("no slots available\n");
    return 0;
}

void close_client_connection(t_client *client)
{
    socket_close(client->socket_fd);
    init_client(client);
}