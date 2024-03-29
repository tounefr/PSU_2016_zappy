/*
** server.h for  in /home/toune/Documents/Epitech/projets/PSU_2016_myirc
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Sun Jun  4 12:04:38 2017 Thomas HENON
** Last update Sat Jul  1 12:31:23 2017 arsene
*/

#ifndef PROJETS_SERVER_H
#define PROJETS_SERVER_H

# define N_NETWORK_COMMANDS 12
# define LOG_PACKET 0
# define LOG_SEND_RECV 0

# define MAX_MAP_WIDTH 30
# define MAX_MAP_HEIGHT 30
# define RESOURCE_MAX_LENGTH 50
# define RESOURCES_NBR_TYPES 9
# define TIME_EGG_HATCHING 600
# define BUFFER_SIZE 2048
# define TEAM_NAME_MAX_LEN 100

# define MAX_CLIENTS 1000
# define MAX_TEAMS 20
# define MAX_PENDING_PACKETS 10
# define MAX_PACKET_SIZE 100
# define MAX_LEVEL 8
# define MAX_EGGS 100

# define DEFAULT_FREQUENCY 100
# define DEFAULT_CLIENTS_PER_TEAM 10
# define DEFAULT_LISTEN_PORT 4242
# define DEFAULT_MAP_WIDTH 10
# define DEFAULT_MAP_HEIGHT 10

# define PLAYER_LIFE_UNITS 10
# define CYCLES_PER_LIFE_UNIT 126

# define TYPE_FOOD 0
# define TYPE_LINEMATE 1
# define TYPE_DERAUMERE 2
# define TYPE_SIBUR 3
# define TYPE_MENDIANE 4
# define TYPE_PHIRAS 5
# define TYPE_THYSTAME 6
# define TYPE_PLAYER 7
# define TYPE_EGG 8

# define ORIENT_NORTH 3
# define ORIENT_SOUTH 1
# define ORIENT_EAST 2
# define ORIENT_WEST 4

#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#include "util.h"
#include "socket.h"
#include "generic_list.h"

# define FLAG_NONE 0
# define FLAG_GUI_CMD 1

typedef struct s_server t_server;
typedef struct s_client t_client;

typedef struct s_cell
{
    int content[9];
} t_cell;

typedef struct s_look
{
    t_cell cell[64];
} t_look;

typedef struct s_network_commands
{
    char *cmd;
    char (*pre_callback)(t_server*, t_client*, char*);
    char (*post_callback)(t_server*, t_client*, char*);
    unsigned int cycles;
    char flags;
} t_network_commands;

# define NBR_LEVELS 7
typedef struct s_incantation
{
    int nb_players;
    int type[RESOURCES_NBR_TYPES];
} t_incantation;

typedef struct s_food
{
    char *s;
    int type;
} t_food;

typedef struct s_pos
{
	int x;
	int y;
} t_pos;

typedef struct s_map
{
	int width;
	int height;
	int cases[MAX_MAP_WIDTH * MAX_MAP_HEIGHT][RESOURCES_NBR_TYPES];
} t_map;

typedef struct s_egg
{
    t_pos pos;
    int num;
    char pending_client;
} t_egg;

typedef struct s_team
{
    char name[TEAM_NAME_MAX_LEN];
    int slots;
} t_team;

typedef struct s_packet
{
    char *raw;
    int remain_cycles;
} t_packet;

typedef struct s_callback
{
    char *packet;
    int cycles;
	char (*func)(t_server*, t_client*, char*);
} t_callback;

typedef struct s_client
{
	int	socket_fd;
    char *buffer;
    unsigned int cur_cycle;
    t_generic_list *callbacks;
    t_generic_list *eggs;
    t_team *team;
    int recv_packet_i;
    int level;
	int num;
	t_pos pos;
	char is_gui;
    char orientation;
    char in_game;
	unsigned char inventory[RESOURCES_NBR_TYPES];
    t_generic_list *read_packets;
	t_generic_list *write_packets;
} t_client;

typedef struct s_server
{
    t_team teams[MAX_TEAMS];
	t_client clients[MAX_CLIENTS];
    int client_lastnum;
    t_client *gui_client;
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
void free_client(t_client *client);
int clients_in_team(t_server *server, t_team *team);
char on_new_client(t_server *server);
void close_client_connection(t_client *client);
char on_exit_client(t_server *server, t_client *client);
void generate_position(t_server *server, t_client *client);

// command.c
char    onPreIncantPacket(t_server *server, t_client *client, char *packet);
char    onPostIncantPacket(t_server *server, t_client *client, char *packet);
char    onSetObjectPacket(t_server *server, t_client *client, char *packet);
char    onTakeObjectPacket(t_server *server, t_client *client, char *packet);
char    onEjectPacket(t_server *server, t_client *client, char *packet);
char    onPreForkPacket(t_server *server, t_client *client, char *packet);
char    onPostForkPacket(t_server *server, t_client *client, char *packet);
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
                 fd_set *fds, fd_set *);
char on_select_read_data(t_server *server, fd_set *fds);
char on_select_write_data(t_server *server, fd_set *fds);

// main.c
t_server *get_server();

// server.c
float cpt_cycle_time(t_server *server);
void init_server(t_server *server);
char listen_server(t_server *server);
char update(t_server *server, struct timeval *last_tick);
char main_loop(t_server *server);

// team.c
char client_assign_team(t_server *server, t_client *client, char *packet);
int clients_in_team(t_server *server, t_team *team);

// util.c
char is_legal_network_char(char c);
char is_numeric(char *s);
int my_rand(int a, int b);
int get_pos(t_server *server, t_pos *pos);
char default_free(void *data);
void free_null(void **data);

// packet.c
char log_packet(int num, char type, char *raw);
void free_packet(t_packet *packet);
char packet_send(t_client *client, char *format, ...);
t_network_commands *get_network_command(char *packet);
char handle_pre_packet(t_server *server, t_client *client);
char handle_post_packet(t_server *server, t_client *client);

// packet2.c
char on_available_data(t_server *server, t_client *client);

// map.c
int get_random_map_pos(t_server *server);
void init_map(t_map *map);

// cycle.c
char is_next_cycle(t_server *server, struct timeval *last_tick);
char packet_pre_cycle(t_server *server, t_client *client);
char packet_post_cycle(t_server *server, t_client *client);

// resources.c
void	take_ressource(t_server *server, int client_pos, int i);
char is_stone(int type);
char generate_resources(t_server *server);

// packet.c
t_network_commands *get_network_command(char *packet);

// incantation.c
char checkIncantationPacket(t_server *server, t_client *client, char *packet);
char    onPreIncantPacket(t_server *server, t_client *client, char *packet);
char    onPostIncantPacket(t_server *server, t_client *client, char *packet);

// gui.c
char gui_send_map_case(t_server *server, int x, int y);
char gui_send_map_content(t_server *server);
char send_client_pos(t_server *server, t_client *client);
char gui_send_teams(t_server *server);
char send_gui_packet(t_server *server, char *packet, ...);
char send_gui_players_connected(t_server *server);

// egg.c
char remove_hatched_egg(t_server *server, t_client *client);
char egg_pending_client(t_server *server, t_client *client);
char lay_egg(t_server *server, t_client *client);
char hatch_egg(t_server *server, t_client *client, char *packet);

// player.c
char onPlayerDead(t_server *server, t_client *client, char *packet);
int get_nb_players_lvl(t_server *server, int level);

// game.c
char on_game_win(t_server *server);

// globals.c
t_food				*get_g_foods();
t_incantation			*get_g_incantations();
t_network_commands		*g_network_commands();

// opts.c
char check_opts_values(t_server *server);
char parse_opts(t_server *server, int ac, char **av);
char usage();

// update.c
char update_client(t_server *server, t_client *client);
char update(t_server *server, struct timeval *last_tick);
char main_loop(t_server *server);

//
void handle_sigint(int signum);

// callback.c
char free_callback(void *data);
t_callback *get_callback(t_client *client,
                         char (*func)(t_server*, t_client*, char*));
char add_callback(t_client *client,
                  char (*func)(t_server*, t_client*, char*),
                  int cycles,
                  void *packet);

char incantationElevation(t_server *server, t_client *client, char *packet);

// look.c
void	debug_count(t_server *s);
char		*look(t_client *client, t_server *server);
int	coordsToIndex(t_server *server, t_pos pos);
void	init_look(t_look *tmp);
void	get_ressources(t_server *s, t_look *see, int index, int pos);
void	lookUp(t_server *s, t_client *c, t_look *see);
void    lookDown(t_server *s, t_client *c, t_look *see);
void    lookLeft(t_server *s, t_client *c, t_look *see);
void    lookRight(t_server *s, t_client *c, t_look *see);
char		*get_type(int i);
char	*myAppend(char *old, char *str);
void	convertView(t_client *c, t_look *see);

#endif //PROJETS_SERVER_H
