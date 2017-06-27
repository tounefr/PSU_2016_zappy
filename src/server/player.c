
#include "server.h"

char check_player_dead(t_server *server, t_client *client)
{
    if (client->life_cycles <= 0) {
        printf("client killed\n");
        packet_send(client->socket_fd, "dead\n");
        send_gui_packet(server, "pdi %d\n", client->num);
        socket_close(client->socket_fd);
        init_client(client);
        return 1;
    }
    return 0;
}