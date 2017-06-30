/*
** main.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:01:16 2017 Thomas HENON
** Last update Fri Jun 23 15:01:17 2017 Thomas HENON
*/

#include <stdlib.h>
#include <signal.h>
#include "server.h"

t_server *get_server()
{
    static t_server *server = NULL;

    if (!server) {
        if (((server = malloc(sizeof(t_server))) == NULL))
            return exit_error(NULL, "malloc error\n");
        init_server(server);
    }
    return server;
}

void handle_sigint(int signum)
{
    int i;
    t_client *client;
    t_server *server;

    exit(1);
    if (!(server = get_server()))
        return;
    for (i = 0; i < MAX_CLIENTS; i++) {
        client = &server->clients[i];
        free_client(client);
    }
    free(server);
    exit(1);
}

int main(int ac, char **av)
{
	t_server *server;
    int returnv;

    (void)ac;
    (void)av;
    srand(time(NULL));
    signal(SIGINT, handle_sigint);
    if (!(server = get_server()))
        return 84;
    if (!parse_opts(server, ac, av))
        return usage();
    returnv = main_loop(server);
    free(server);
    return (returnv ? 0 : 84);
}
