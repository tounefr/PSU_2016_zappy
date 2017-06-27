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

static float timedifference_msec(struct timeval t0, struct timeval t1)
{
    return (t1.tv_sec - t0.tv_sec) * 1000.0f +
            (t1.tv_usec - t0.tv_usec) / 1000.0f;
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