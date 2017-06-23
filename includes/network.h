
#ifndef PROJETS_NETWORK_H
#define PROJETS_NETWORK_H

# define FLAG_NONE 0
# define FLAG_GUI_CMD 1

typedef struct s_network_commands
{
    char *cmd;
    char (*callback)(t_server*, t_client*, char*);
    char flags;
} t_network_commands;
extern t_network_commands network_commands[N_NETWORK_COMMANDS];

#endif //PROJETS_NETWORK_H
