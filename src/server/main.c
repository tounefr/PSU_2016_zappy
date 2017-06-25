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

char usage()
{
    printf("USAGE: ./zappy_server -p port -x width"
                   " -y height -n name1 name2 ... -c clientsNb "
                   "-f freq\n"
                   "\tport      is the port number\n"
                   "\twidth     is the width of the world\n"
                   "\theight    is the height of the world\n"
                   "\tnameX     is the name of the team X\n"
                   "\tclientsNb is the number of authorized clients per team\n"
                   "\tfreq      is the reciprocal of time unit for execution of actions\n");
    return 0;
}

char parse_team_names(t_server *server, int *i, int ac, char **av)
{
    int i2;
    int i3;

    i3 = 0;
    for (i2 = *i + 1; i2 < ac && av[i2][0] != '-'; i2++)
        strncpy(&server->teams_name[i3++], av[i2], TEAM_NAME_MAX_LEN - 1);
    *i = i2;
}

char check_opts_values(t_server *server)
{
    if (server->freq < 2 || server->freq > 10000)
        return exit_error(0, "\n-f option only accepts integer values between 2 and 10000\n\n");
    if (server->map.width < 10 || server->map.width > 30)
        return exit_error(0, "\n-x option only accepts integer values between 10 and 30\n\n");
    if (server->map.height < 10 || server->map.height > 30)
        return exit_error(0, "\n-y option only accepts integer values between 10 and 30\n\n");
    if (server->clients_per_team < 1)
        return exit_error(0, "\n-c option only accepts integer values greater or equal to 1\n\n");
    return 1;
}

char parse_opts(t_server *server, int ac, char **av)
{
    int i;

    for (i = 1; i < ac; i++) {
        if (!strcmp(av[i], "-help"))
            return 0;
        if (i + 1 < ac) {
            if (!strcmp(av[i], "-p") && is_numeric(av[i + 1]))
                server->listen_port = atoi(av[i + 1]);
            if (!strcmp(av[i], "-x") && is_numeric(av[i + 1]))
                server->map.width = atoi(av[i + 1]);
            if (!strcmp(av[i], "-y") && is_numeric(av[i + 1]))
                server->map.height = atoi(av[i + 1]);
            if (!strcmp(av[i], "-c") && is_numeric(av[i + 1]))
                server->clients_per_team = atoi(av[i + 1]);
            if (!strcmp(av[i], "-f") && is_numeric(av[i + 1]))
                server->freq = atoi(av[i + 1]);
            if (!strcmp(av[i], "-n"))
                parse_team_names(server, &i, ac, av);
        }
    }
    return check_opts_values(server);
}

int main(int ac, char **av)
{
	t_server *server;
    int returnv;

    (void)ac;
    (void)av;
    if ((server = malloc(sizeof(t_server))) == NULL)
        return exit_error(84, "malloc error\n");
	init_server(server);
    if (!parse_opts(server, ac, av))
        return usage();
    returnv = main_loop(server);
    free(server);
    return (returnv ? 0 : 84);
}
