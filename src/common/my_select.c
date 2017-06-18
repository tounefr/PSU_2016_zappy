/*
** my_select.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_myirc
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sun Jun  4 12:02:20 2017 Thomas HENON
** Last update Sun Jun  4 12:02:22 2017 Thomas HENON
*/

#include "common.h"

void
init_my_select(t_my_select *server_select)
{
    server_select->timeout.tv_sec = 0;
    server_select->timeout.tv_usec = 5000;
    server_select->nfds = -1;
    server_select->readfds_n = 0;
    server_select->writefds_n = 0;
    FD_ZERO(&server_select->readfds);
    FD_ZERO(&server_select->writefds);
}

void
add_readfd_my_select(t_my_select *server_select,
                     int fd)
{
    FD_SET(fd, &server_select->readfds);
    if (fd > server_select->nfds)
        server_select->nfds = fd + 1;
    server_select->readfds_n++;
}
