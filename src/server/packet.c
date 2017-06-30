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
# define _GNU_SOURCE
#include <stdio.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include "server.h"

void free_packet(t_packet *packet)
{
    free(packet->raw);
}

char packet_send(t_client *client, char *format, ...)
{
    char *buffer;
    va_list args;

    if (client->is_gui)
        return 0;
    va_start(args, format);
    printf("Send>> ");
    vprintf(format, args);
    va_end(args);
    va_start(args, format);
    if (vasprintf(&buffer, format, args) == -1) {
        va_end(args);
        return exit_error(0, "malloc error\n");
    }
    va_end(args);
    if (!generic_list_append(&client->write_packets, buffer))
        return exit_error(0, "malloc error\n");
    return 1;
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

char handle_pre_packet(t_server *server, t_client *client)
{
    char *packet;
    t_network_commands *net_cmd;
    t_callback *callback;

    if (!client->read_packets)
        return 1;
    packet = generic_list_pop(&client->read_packets);
    client->recv_packet_i++;
    if (client->recv_packet_i == 1)
        return on_welcome(server, client, packet);
    if (!(net_cmd = get_network_command(packet)) ||
            !(callback = malloc(sizeof(t_callback)))) {
        free(packet);
        return exit_error(0, "Unknown packet\n");
    }
    callback->packet = packet;
    callback->remain_cycles = net_cmd->cycles;
    callback->func = net_cmd->post_callback;
    printf("precycle %s\n", net_cmd->cmd);
    generic_list_append(&client->callbacks, callback);
    return 1;
}

char handle_post_packet(t_server *server, t_client *client)
{
    t_network_commands *net_cmd;
    t_generic_list *node;
    t_callback *callback;

    node = client->callbacks;
    while (node)
    {
        callback = node->data;
        callback->remain_cycles--;
        if (callback->remain_cycles <= 0) {
            printf("postcycle %s\n", callback->packet);
            callback->func(server, client, callback->packet);
            node = node->next;
            generic_list_remove(&client->callbacks, callback, free);
            continue;
        }
        node = node->next;
    }
    return 1;
}