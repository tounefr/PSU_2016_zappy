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
    returnv = dprintf(fd, format, args);
    printf("Send>> %s", format);
    va_end(args);
    return returnv;
}

t_network_commands *get_network_command(char *packet)
{
    int i;

    for (i = 0; i < N_NETWORK_COMMANDS; i++) {
        if (!strncmp(network_commands[i].cmd, packet,
                     strlen(network_commands[i].cmd)) &&
            network_commands[i].callback)
            return &network_commands[i];
    }
    return NULL;
}

char stack_packet(t_server *server, t_client *client, char *packet)
{
    int i2;
    t_network_commands *net_cmd;

    for (i2 = 0; i2 < MAX_PENDING_PACKETS; i2++) {
        if (client->pending_packets[i2])
            continue;
        client->pending_packets[i2] = get_network_command(packet);
        if (!client->pending_packets[i2])
            return exit_error(0, "get_network_command failed\n");
        printf("Recv<< %s\n", packet);
        return 1;
    }
    return exit_error(0, "no slots available\n");
}

void alloc_packet(t_server *server, t_client *client, int i, char *packet)
{
    memcpy(packet, &client->buffer, i);
    if (i + 1 < BUFFER_SIZE) {
        memmove(&client->buffer, &client->buffer[i + 1],
                strlen(&client->buffer[i + 1]) + 2);
        memset(&client->buffer + strlen(client->buffer), 0,
               BUFFER_SIZE - strlen(client->buffer));
    } else
        memset(&client->buffer, 0, BUFFER_SIZE);
}

char on_packet(t_server *server, t_client *client, int i)
{
    char packet[BUFFER_SIZE];

    memset(packet, 0, BUFFER_SIZE);
    alloc_packet(server, client, i, &packet);
    client->recv_packet_i++;
    if (client->recv_packet_i == 1)
        return on_welcome(server, client, packet);
    return stack_packet(server, client, packet);
}

char on_available_data(t_server *server, t_client *client)
{
    int buff_av_size;
    char *buffer;
    int i;
    int recvrv;
    int retv;

    buff_av_size = BUFFER_SIZE - strlen((char*)&client->buffer);
    if (buff_av_size < 0)
        return exit_error(0, "unknown packet : data too long\n");
    buffer = (char*)&client->buffer + strlen((char*)client->buffer);
    if ((recvrv = recv(client->socket_fd, buffer, buff_av_size - 1, 0)) == -1)
        return exit_error(0, "recv error : %s\n", strerror(errno));
    else if (recvrv == 0)
        return exit_error(0, "recv error : no data\n");
    do {
        retv = 0;
        for (i = 0; i < BUFFER_SIZE && buffer[i] != 0; i++) {
            if (i < recvrv && is_legal_network_char(buffer[i]))
                return exit_error(0, "unknown packet : illegal char: %d\n", buffer[i]);
            if (client->buffer[i] == '\n') {
                on_packet(server, client, i);
                retv = 1;
                break;
            }
        }
    } while (retv);
    return 1;
}
