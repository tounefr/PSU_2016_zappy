/*
** cycle.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Sat Jun 24 15:38:05 2017 Thomas HENON
** Last update Sat Jun 24 15:38:06 2017 Thomas HENON
*/

#include <time.h>
#include "server.h"

float timedifference_msec(struct timeval t0, struct timeval t1)
{
    return (t1.tv_sec - t0.tv_sec) * 1000.0f + (t1.tv_usec - t0.tv_usec) / 1000.0f;
}

char is_next_cycle(t_server *server, struct timeval *last_tick)
{
    struct timeval cur_time;
    float elapsed;

    gettimeofday(&cur_time, 0);
    elapsed = timedifference_msec(*last_tick, cur_time);
    if (elapsed >= server->cycle_time) {
        server->cur_cycle++;
        gettimeofday(last_tick, 0);
        return 1;
    }
    return 0;
}

char packet_pre_cycle(t_client *client)
{
    int i;
    t_network_commands *net_cmd;

    for (i = 0; i < MAX_PENDING_PACKETS; i++) {
        if (strlen(client->pending_packets[i]) > 0) {
            client->cur_packet = &client->pending_packets[i];
            printf("Precycle %s\n", client->cur_packet);
            if (!(net_cmd = get_network_command(client->cur_packet)))
                continue;
            client->remain_cycles = net_cmd->cycles;
            return 1;
        }
    }
    return 0;
}

char packet_post_cycle(t_server *server, t_client *client)
{
    int i;
    int i2;

    t_network_commands *net_cmd;

    for (i = 0; i < MAX_PENDING_PACKETS; i++) {
        if (&client->pending_packets[i] == client->cur_packet) {
            if (!(net_cmd = get_network_command(client->cur_packet)))
                continue;
            net_cmd->callback(server, client, client->cur_packet);
            client->remain_cycles = -1;
            printf("Postcycle %s\n", client->cur_packet);
            memset(client->cur_packet, 0, BUFFER_SIZE);
            for (i2 = i + 1; i2 < MAX_PENDING_PACKETS; i2++) {
                if (strlen(client->pending_packets[i]) > 0) {
                    client->cur_packet = &client->pending_packets[i2];
                    return 1;
                }
            }
            client->cur_packet = NULL;
            return 1;
        }
    }
    return 0;
}