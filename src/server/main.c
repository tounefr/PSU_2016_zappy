
/*
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <sys/socket.h>
#include <unistd.h>
#include <fcntl.h>
*/

#include "server.h"
#include "network.h"

int main(int ac, char **av)
{
	t_server server;

	(void)ac;
	(void)av;
	init_server(&server);
    main_loop(&server);

}