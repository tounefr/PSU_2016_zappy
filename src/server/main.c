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
#include "server.h"

int main(int ac, char **av)
{
	t_server *server;
    int returnv;

    (void)ac;
    (void)av;
    printf("server in mem size : %d bytes\n", sizeof(*server));
    if ((server = malloc(sizeof(t_server))) == NULL)
        return exit_error(84, "malloc error\n");
	init_server(server);
    returnv = main_loop(server);
    free(server);
    return (returnv ? 0 : 84);
}
