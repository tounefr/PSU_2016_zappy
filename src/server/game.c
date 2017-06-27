/*
** game.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Mon Jun 26 22:58:42 2017 Thomas HENON
** Last update Mon Jun 26 22:58:42 2017 Thomas HENON
*/

#include "server.h"

char on_game_win(t_server *server)
{
    int i;
    t_client *client;

    for (i = 0; i < MAX_CLIENTS; i++) {
        client = &server->clients[i];
        if (client->socket_fd == -1)
            continue;
        packet_send(client->socket_fd, "dead\n");
        socket_close(client->socket_fd);
        init_client(client);
    }
}