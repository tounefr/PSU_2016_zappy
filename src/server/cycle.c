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

    for (i = 0; i < MAX_PENDING_PACKETS; i++) {
        if (client->pending_packets[i]) {
            client->cur_packet = client->pending_packets[i];
            client->remain_cycles = client->cur_packet->cycles;
            return 1;
        }
    }
    return 0;
}

char packet_post_cycle(t_server *server, t_client *client)
{
    int i;

    for (i = 0; i < MAX_PENDING_PACKETS; i++) {
        if (client->cur_packet == client->pending_packets[i]) {
            client->pending_packets[i] = NULL;
            client->cur_packet->callback(server, client, client->cur_packet->cmd);
            client->remain_cycles = -1;
            client->cur_packet = NULL;
            return 1;
        }
    }
    return 0;
}