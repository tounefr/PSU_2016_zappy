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

char onPlayerDead(t_server *server, t_client *client, char *packet)
{
    (void)packet;
    printf("player dead\n");
    packet_send(client, "dead\n");
    on_exit_client(server, client);
    return 1;
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
