
#include <stdlib.h>
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

int main(int ac, char **av)
{

}