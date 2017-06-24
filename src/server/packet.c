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
#include "network.h"

char packet_send(int fd, char *format, ...)
{
    va_list args;
    int returnv;

    va_start(args, format);
    returnv = dprintf(fd, format, args);
    printf("Send>> %s", format);
    va_end(args);
    return returnv;
}

char packet_callback(t_server *server, t_client *client, char *packet)
{
    int i;

    for (i = 0; i < N_NETWORK_COMMANDS; i++) {
        if (!strncmp(network_commands[i].cmd, packet,
                     strlen(network_commands[i].cmd)) &&
                network_commands[i].callback)
            return network_commands[i].callback(server, client, packet);
    }
    return exit_error(0, "unknown packet\n");
}

char packet_route(t_server *server, t_client *client, char *packet)
{
    client->packet_i++;
    if (client->packet_i == 1)
        return on_welcome(server, client, packet);
    return packet_callback(server, client, packet);
}

char on_packet(t_server *server, t_client *client, int i, char *packet)
{
    memcpy(packet, &client->buffer, i);
    if (i + 1 < BUFFER_SIZE) {
        memmove(&client->buffer, &client->buffer[i + 1],
                BUFFER_SIZE - i + 1);
        memset(&client->buffer + strlen(client->buffer), 0,
               BUFFER_SIZE - strlen(client->buffer));
    } else
        memset(&client->buffer, 0, BUFFER_SIZE);
    printf("Recv<< %s\n", packet);
    return packet_route(server, client, packet);
}

char on_available_data(t_server *server, t_client *client)
{
    int buff_av_size;
    char packet[BUFFER_SIZE];
    char *buffer;
    int i;
    int recvrv;

    buff_av_size = BUFFER_SIZE - strlen((char*)&client->buffer);
    if (buff_av_size < 0)
        return exit_error(0, "unknown packet : data too long\n");
    memset(packet, 0, BUFFER_SIZE);
    buffer = (char*)&client->buffer + strlen((char*)client->buffer);
    if ((recvrv = recv(client->socket_fd, buffer, buff_av_size, 0)) == -1)
        return exit_error(0, "recv error : %s\n", strerror(errno));
    else if (recvrv == 0)
        return exit_error(0, "recv error : no data\n");
    for (i = 0; i < BUFFER_SIZE; i++) {
        if (i < recvrv && is_legal_network_char(buffer[i]))
            return exit_error(0, "unknown packet : illegal char\n");
        if (client->buffer[i] == '\n')
            return on_packet(server, client, i, (char*)&packet);
    }
    return 0;
}
