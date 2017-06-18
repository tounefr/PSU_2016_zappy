/*
** socket.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_myftp
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Thu May 18 10:30:28 2017 Thomas HENON
** Last update Thu May 18 10:30:30 2017 Thomas HENON
*/

#include <arpa/inet.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include "util.h"
#include "socket.h"

int
socket_init()
{
    int fd;

    if (-1 == (fd = socket(AF_INET, SOCK_STREAM, 0)))
        return exit_error(-1, "socket : %s\n", strerror(errno));
    return fd;
}

char
socket_connect(int fd,
               char *ip,
               unsigned short *port)
{
    struct sockaddr_in  sockaddr;
    socklen_t           socksize;

    sockaddr.sin_family = AF_INET;
    sockaddr.sin_port = htons(*port);
    inet_pton(AF_INET, ip, &(sockaddr.sin_addr));
    socksize = sizeof(sockaddr);
    if (-1 == connect(fd, (struct sockaddr *)&sockaddr, socksize))
        return exit_error(0, "connect : %s\n", strerror(errno));
    return 1;
}

char socket_infos(int socket_fd,
                  t_socket_infos *socket_infos)
{
    struct sockaddr_in  sockaddr;
    socklen_t           socksize;

    socksize = sizeof(sockaddr);
    if (-1 == getpeername(socket_fd, (struct sockaddr*)&sockaddr, &socksize))
        return exit_error(0, "getpeername failed\n");
    socket_infos->client_ipv4 = my_strdup(inet_ntoa(sockaddr.sin_addr));
    socket_infos->client_port = sockaddr.sin_port;
    memset(socket_infos->client_hostname, 0,
           sizeof(socket_infos->client_hostname));
    memset(&sockaddr, 0, sizeof(struct sockaddr_in));
    if (-1 == getsockname(socket_fd, (struct sockaddr*)&sockaddr, &socksize))
        return exit_error(0, "getsockname failed\n");
    socket_infos->server_ipv4 = my_strdup(inet_ntoa(sockaddr.sin_addr));
    assert(socket_infos->client_ipv4 != NULL &&
                   socket_infos->server_ipv4 != NULL);
    socket_infos->server_port = sockaddr.sin_port;
    return 1;
}

char
socket_send(int fd,
            char *buffer)
{
    if (-1 == write(fd, buffer, strlen(buffer) + 1))
        return exit_error(0, "write error : %s\n", strerror(errno));
    return 1;
}

char socket_close(int fd)
{
    shutdown(fd, SHUT_RDWR);
    close(fd);
    return 1;
}
