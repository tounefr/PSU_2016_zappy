/*
** socket.h for  in /home/toune/Documents/Epitech/projets/PSU_2016_myirc
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sun May 28 00:04:00 2017 Thomas HENON
** Last update Sun May 28 00:04:01 2017 Thomas HENON
*/

#ifndef PROJETS_SOCKET_H
#define PROJETS_SOCKET_H

typedef struct s_socket_infos
{
    char            *client_ipv4;
    unsigned short  client_port;
    char            client_hostname[1024];
    char            *server_ipv4;
    unsigned short  server_port;
} t_socket_infos;

void
free_socket_infos(t_socket_infos *socket_infos);
char*
resolve_hostname(char *host);
int socket_init();
char socket_connect(int fd, char *ip, unsigned short *port);
char socket_infos(int socket_fd, t_socket_infos *socket_infos);
char socket_send(int fd, char *buffer);
char socket_close(int fd);
char socket_port_used(unsigned short port);

int socket_accept(int server_socket);
char socket_listen(int server_fd,
                   char *listen_address,
                   unsigned short *listen_port);
char
socket_nbsend(int fd, char *buffer);
char *last_error();

#endif //PROJETS_SOCKET_H
