/*
** packet.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:01:20 2017 Thomas HENON
** Last update Fri Jun 23 15:01:20 2017 Thomas HENON
*/

#include <string.h>
#include <stdio.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include "server.h"

char packet_send(int fd, char *format, ...)
{
    va_list args;
    int returnv;

    va_start(args, format);
    printf("Send>> ");
    vprintf(format, args);
    va_end(args);
    va_start(args, format);
    returnv = vdprintf(fd, format, args);
    va_end(args);
    return returnv;
}

t_network_commands *get_network_command(char *packet)
{
    int i;

    for (i = 0; i < N_NETWORK_COMMANDS; i++) {
        if (!strncmp(g_network_commands()[i].cmd, packet,
                     strlen(g_network_commands()[i].cmd)))
            return &g_network_commands()[i];
    }
    return NULL;
}

int stack_packet(t_server *server, t_client *client, char *packet)
{
    int i2;

    (void)server;
    for (i2 = 0; i2 < MAX_PENDING_PACKETS; i2++) {
        if (strlen(client->pending_packets[i2]) > 0)
            continue;
        strncpy((char*)&client->pending_packets[i2], packet, BUFFER_SIZE - 1);
        return i2;
    }
    return exit_error(-1, "no slots available\n");
}

char alloc_packet(t_server *server, t_client *client, int i, char *packet)
{
    (void)server;
    memset(packet, 0, BUFFER_SIZE);
    memcpy(packet, &client->buffer, BUFFER_SIZE - 1);
    if (i + 1 < BUFFER_SIZE) {
        memmove(&client->buffer, &client->buffer[i + 1],
                strlen(&client->buffer[i + 1]) + 2);
        memset(&client->buffer + strlen(client->buffer), 0,
               BUFFER_SIZE - strlen(client->buffer));
    } else
        memset(&client->buffer, 0, BUFFER_SIZE);
    packet[i] = '\0';
    return 1;
}

char on_packet(t_server *server, t_client *client, int i)
{
    int i2;
    char packet[BUFFER_SIZE];

    if (!alloc_packet(server, client, i, (char*)&packet))
        return 0;
    printf("Recv<< %s\n", (char*)&packet);
    client->recv_packet_i++;
    if (client->recv_packet_i == 1)
        return on_welcome(server, client, (char*)&packet);
    if (!get_network_command((char*)&packet))
        return exit_error(0, "Unknown packet\n");
    if ((i2 = stack_packet(server, client, (char*)&packet)) == -1)
        return 0;
    return 1;
}