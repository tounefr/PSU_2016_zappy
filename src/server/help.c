//
// Created by arsene on 6/20/17.
//

#include <stdio.h>

void    display_help()
{
	printf("USAGE: ./zappy_server -p port -x width -y height -n name1 name2 ...");
	printf("-c clientsNb -f freq\n\tport\t  is the port number\n\twidth\t");
	printf("  is the width of the world\n\theight\t  is the height of the world\n");
	printf("\tnameX\t  is the name of the team X\n\tclientsNb is the number");
	printf(" of authorized clients per team\n\tfreq\t  is the reciprocal of time");
	printf(" unit for execution of actions\n");
}