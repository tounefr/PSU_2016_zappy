/*
** main.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:01:16 2017 Thomas HENON
** Last update Fri Jun 23 15:01:17 2017 Thomas HENON
*/

#include "server.h"
#include "network.h"

int main(int ac, char **av)
{
	t_server server;

	(void)ac;
	(void)av;
	init_server(&server);
    return (main_loop(&server) ? 0 : 84);
}
