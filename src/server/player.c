/*
** player.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Mon Jun 26 23:43:01 2017 Thomas HENON
** Last update Mon Jun 26 23:43:01 2017 Thomas HENON
*/

#include "server.h"

char check_player_dead(t_server *server, t_client *client)
{
    if (client->life_cycles <= 0) {
        printf("client killed\n");
        packet_send(client, "dead\n");
        send_gui_packet(server, "pdi %d\n", client->num);
        socket_close(client->socket_fd);
        init_client(client);
        return 1;
    }
    return 0;
}

int get_nb_players_lvl(t_server *server, int level)
{
    int i;
    t_client *client;
    int c;

    c = 0;
    for (i = 0; i < MAX_CLIENTS; i++) {
        client = &server->clients[i];
        if (client->socket_fd == -1)
            continue;
        if (client->level == level)
            c++;
    }
    return c;
}
