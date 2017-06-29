/*
** packet2.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Mon Jun 26 23:29:06 2017 Thomas HENON
** Last update Mon Jun 26 23:29:07 2017 Thomas HENON
*/

#include <sys/types.h>
#include <sys/socket.h>
#include "server.h"

static char increase_buffer(t_server *server, t_client *client, char *buffer)
{
    int len;

    if (!client->buffer) {
        client->buffer = buffer;
        return 1;
    } else {
        len = strlen(client->buffer) + strlen(buffer) + 1;
        if (!(client->buffer = realloc(client->buffer, len)))
            return exit_error(0, "malloc error\n");
        client->buffer[len - 1] = '\0';
        strcpy(client->buffer + strlen(client->buffer), buffer);
    }
    return 1;
}

static char split_buffer(t_server *server, t_client *client)
{
    int i;
    int len;
    int start;
    char *packet;

    len = strlen(client->buffer);
    start = 0;
    for (i = 0; i < len; i++) {
        if (client->buffer[i] == '\n') {
            client->buffer[i] = '\0';
            if (!(packet = strdup(&client->buffer[start])))
                return exit_error(0, "malloc error\n");
            start = i + 1;
            printf("Recv<< %s\n", packet);
            if (!generic_list_append(&client->read_packets, packet))
                return exit_error(0, "malloc error\n");
            start = i + 1;
        }
    }
    if (client->buffer)
        free(client->buffer);
    if (!(client->buffer = strdup(&client->buffer[start])))
        return exit_error(0, "malloc error\n");
    return 1;
}

char on_available_data(t_server *server, t_client *client)
{
    char *buffer;
    int recvrv;

    if (!(buffer = malloc(BUFFER_SIZE))) {
        on_exit_client(server, client);
        return exit_error(0, "malloc error\n");
    }
    memset(buffer, 0, BUFFER_SIZE);
    if ((recvrv = recv(client->socket_fd, buffer, BUFFER_SIZE - 1, 0)) <= 0) {
        free(buffer);
        on_exit_client(server, client);
        if (recvrv == 0)
            return exit_error(0, "recv error: no data\n");
        return exit_error(0, "recv error : %s\n", strerror(errno));
    }
    if (!increase_buffer(server, client, buffer) ||
            !split_buffer(server, client)) {
        free(buffer);
        on_exit_client(server, client);
        return 0;
    }
    free(buffer);
    return 1;
}