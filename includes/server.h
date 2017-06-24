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

# define N_NETWORK_COMMANDS 12

# define MAX_MAP_HEIGHT 30
# define RESOURCE_MAX_LENGTH 50
# define RESOURCES_NBR_TYPES 7
# define BUFFER_SIZE 2048
# define TEAM_NAME_MAX_LEN 100
# define MAX_CLIENTS 1000
# define MAX_TEAMS 20

# define DEFAULT_FREQUENCY 100
# define DEFAULT_MAP_SIZE 30
# define DEFAULT_CLIENTS_PER_TEAM 10
# define DEFAULT_LISTEN_PORT 4242

# define TYPE_PLAYER 0
# define TYPE_LINEMATE 1
# define TYPE_DERAUMERE 2
# define TYPE_SIBUR 3
# define TYPE_MENDIANE 4
# define TYPE_PHIRAS 5
# define TYPE_THYSTAME 6
# define TYPE_FOOD 7

# define ORIENTATION_LEFT 1
# define ORIENTATION_RIGHT 2
# define ORIENTATION_TOP 3
# define ORIENTATION_BOTTOM 4

#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#include "util.h"
#include "socket.h"

typedef struct s_pos
{
	int x;
	int y;
} t_pos;

typedef struct s_map
{
	int width;
	int height;
	int cases[MAX_MAP_HEIGHT * MAX_MAP_HEIGHT][RESOURCES_NBR_TYPES];
} t_map;

typedef struct s_client
{
	int	socket_fd;
	char buffer[BUFFER_SIZE];
	int team_i;
	int packet_i;
	int client_num;
	t_pos pos;
	char is_gui;
    char orientation;
	unsigned char inventory[RESOURCES_NBR_TYPES];
} t_client;

typedef struct s_server
{
	char teams_name[MAX_TEAMS][TEAM_NAME_MAX_LEN];
	t_client clients[MAX_CLIENTS];
    int server_fd;
	float freq;
	unsigned short listen_port;
	t_map map;
    float cycle_time;
    unsigned int cur_cycle;
	unsigned int clients_per_team;
} t_server;


// client.c
void init_client(t_client *client);
int clients_in_team(t_client *clients, int team_i);
char on_new_client(t_server *server);
void close_client_connection(t_client *client);

// command.c
char    onIncantationPacket(t_server *server, t_client *client, char *packet);
char    onSetObjectPacket(t_server *server, t_client *client, char *packet);
char    onTakeObjectPacket(t_server *server, t_client *client, char *packet);
char    onEjectPacket(t_server *server, t_client *client, char *packet);
char    onForkPacket(t_server *server, t_client *client, char *packet);
char    onConnectNbrPacket(t_server *server, t_client *client, char *packet);
char    onBroadcastPacket(t_server *server, t_client *client, char *packet);
char    onInventoryPacket(t_server *server, t_client *client, char *packet);
char    onForwardPacket(t_server *server, t_client *client, char *packet);
char    onRightPacket(t_server *server, t_client *client, char *packet);
char    onLeftPacket(t_server *server, t_client *client, char *packet);
char    onLookPacket(t_server *server, t_client *client, char *packet);

char on_welcome(t_server *server, t_client *client, char *packet);

// select.c
void select_init(t_server *server, int *nfds,
                 fd_set *fds, struct timeval *timeout);
char on_select_data(t_server *server, fd_set *fds);

// server.c
void init_server(t_server *server);
char listen_server(t_server *server);
char main_loop(t_server *server);

// team.c
int get_team_name_index(t_server *server, char *team_name);

// util.c
char is_legal_network_char(char c);

// packet.c
char packet_send(int fd, char *format, ...);
char packet_callback(t_server *server, t_client *client, char *packet);
char packet_route(t_server *server, t_client *client, char *packet);
char on_packet(t_server *server, t_client *client, int i, char *packet);
char on_available_data(t_server *server, t_client *client);

// map.c
void init_map(t_map *map);

// cycle.c
char is_next_cycle(t_server *server, struct timeval *last_tick);

/*
typedef struct      s_server
{
	int             port_number;
	int             x;
	int             y;
	char            *team_names;
	int             clientsNb;
	int             timeUnit;
}                   t_server;
 */

//void                display_help();
//char                display_error(int);

#endif //PROJETS_SERVER_H
