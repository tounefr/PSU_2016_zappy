/*
** server.h for  in /home/toune/Documents/Epitech/projets/PSU_2016_myirc
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sun Jun  4 12:04:38 2017 Thomas HENON
** Last update Sun Jun  4 12:04:39 2017 Thomas HENON
*/

#ifndef PROJETS_SERVER_H
#define PROJETS_SERVER_H

# define N_NETWORK_COMMANDS 13

typedef struct      s_server
{
	int             port_number;
	int             x;
	int             y;
	char            *team_names;
	int             clientsNb;
	int             timeUnit;
}                   t_server;

void                display_help();
void                display_error(int);

#endif //PROJETS_SERVER_H
