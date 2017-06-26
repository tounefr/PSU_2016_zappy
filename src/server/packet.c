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
        if (!strncmp(g_network_commands[i].cmd, packet,
                     strlen(g_network_commands[i].cmd)))
            return &g_network_commands[i];
    }
    return NULL;
}

int stack_packet(t_server *server, t_client *client, char *packet)
{
    int i2;

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
                if (!on_packet(server, client, i))
                    return 0;
                retv = 1;
                break;
            }
        }
    } while (retv);
    return 1;
}
