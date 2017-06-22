//
// Created by arsene on 6/20/17.
//

#include <stdlib.h>
#include "server.h"

int         coordinates_assign(char **args, int i, t_server server)
{
	if (check_atoi(args[i + 1]) == 0)
		server.x = atoi(args[i + 1]);
	else
		return (84);
	if (args[i + 2] == NULL)
		display_error(1);
	if (strcmp("-y", args[i + 2]) == 0)
	{
		if (check_atoi(args[i + 3]) == 0)
			server.y = atoi(args[i + 3]);
		else
			return (84);
	}
	else
		return (84);
	return (0);
}

int         port_number(char **args, int i, t_server server)
{
	if (check_atoi(args[i + 1]) == 0)
		server.port_number = atoi(args[i + 1]);
	else
		return (84);
	return (0);
}