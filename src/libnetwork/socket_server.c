/*
** socket_server.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_myftp
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Thu May 18 10:30:59 2017 Thomas HENON
** Last update Thu May 18 10:30:59 2017 Thomas HENON
*/

#include <arpa/inet.h>
#include <sys/socket.h>
#include "util.h"

int
socket_accept(int server_socket)
{
    struct sockaddr_in  sin;
    int client_socket;
    socklen_t           sinsize;

    sinsize = sizeof(struct sockaddr_in);
    client_socket = accept(server_socket, (struct sockaddr*)&sin, &sinsize);
    if (-1 == client_socket)
        return exit_error(-1, "accept error : %s\n", strerror(errno));
    return client_socket;
}

char socket_listen(int server_fd,
                   char *listen_address,
                   unsigned short *listen_port)
{
    struct sockaddr_in  sockaddr;
    int                 option;

    option = -1;
    if (-1 == setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR,
                         &option, sizeof(option)))
        return exit_error(0, "setsockopt error : %s\n", strerror(errno));
    if (-1 == setsockopt(server_fd, SOL_SOCKET, SO_REUSEPORT,
                         &option, sizeof(option)))
        return exit_error(0, "setsockopt error : %s\n", strerror(errno));
    sockaddr.sin_family = AF_INET;
    sockaddr.sin_port = htons(*listen_port);
    inet_aton(listen_address, &sockaddr.sin_addr);
    if (-1 == bind(server_fd, (struct sockaddr*)&sockaddr,
                   sizeof(sockaddr)))
        return exit_error(0, "bind error : %s\n", strerror(errno));
    if (-1 == listen(server_fd, 42))
        return exit_error(0, "listen error : %s\n", strerror(errno));
    return 1;
}
