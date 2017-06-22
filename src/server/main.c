
#include <stdlib.h>
#include <string.h>
#include "server.h"
#include "network.h"

t_network_commands network_commands[N_NETWORK_COMMANDS] =
{
        { "Forward", NULL, FLAG_NONE },
        { "Right", NULL, FLAG_NONE },
        { "Left", NULL, FLAG_NONE },
        { "Look", NULL, FLAG_NONE },
        { "Inventory", NULL, FLAG_NONE },
        { "Broadcast", NULL, FLAG_NONE },
        { "Connect_nbr", NULL, FLAG_NONE },
        { "Fork", NULL, FLAG_NONE },
        { "Eject", NULL, FLAG_NONE },
        { "Take object", NULL, FLAG_NONE },
        { "Set object", NULL, FLAG_NONE },
        { "Incantation", NULL, FLAG_NONE },
        { "GRAPHIC", NULL, FLAG_GUI_CMD },
};

int                 check_atoi(char *str)
{
	unsigned int    i;

	i = 0;
	while (i < strlen(str))
	{
		if (!(str[i] - 48 >= 0 && str[i] - 48 <= 9))
			return (84);
		i++;
	}
	return (0);
}

int                 check_args(char **args, int numberargs)
{
	int             i;
	t_server        *server;

	if ((server = malloc(sizeof(t_server))) == NULL)
		return (1);
	i = 0;
	if (strcmp(args[1], "-help") == 0)
		display_help();
	while (i < numberargs)
	{
		if (strcmp(args[i], "-p") == 0)
			if (port_number(args, i, server) == 84)
				display_error(1);
		if (strcmp(args[i], "-x") == 0)
			if (coordinates_assign(args, i, server) == 84)
				display_error(1);
		
		i++;
	}
	return (0);
}

int                 main(int ac, char **av)
{
	if (ac < 2)
		display_error(1);
	if (check_args(av, ac) == 4)
		return 0;
	if (check_args(av, ac) == 0)
	{}

}