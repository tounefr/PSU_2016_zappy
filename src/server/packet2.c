/*
** packet2.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Mon Jun 26 23:29:06 2017 Thomas HENON
** Last update Mon Jun 26 23:29:07 2017 Thomas HENON
*/

#include "server.h"

static char on_available_data2(t_server *server,
                               t_client *client,
                               int recvrv,
                               char *buffer)
{
    int retv;
    int i;

    do {
        retv = 0;
        for (i = 0; i < BUFFER_SIZE && buffer[i] != 0; i++) {
            if (i < recvrv && is_legal_network_char(buffer[i])) {
                on_exit_client(server, client);
                return exit_error(0, "unknown packet : illegal char: %d\n",
                                  buffer[i]);
            }
            if (client->buffer[i] == '\n') {
                if (!on_packet(server, client, i)) {
                    on_exit_client(server, client);
                    return 0;
                }
                retv = 1;
                break;
            }
        }
    } while (retv);
    return 1;
}

char on_available_data(t_server *server, t_client *client)
{
    int buff_av_size;
    char *buffer;
    int recvrv;
    int retv;

    buff_av_size = BUFFER_SIZE - strlen((char*)&client->buffer);
    if (buff_av_size < 0) {
        on_exit_client(server, client);
        return exit_error(0, "unknown packet : data too long\n");
    }
    buffer = (char*)&client->buffer + strlen((char*)client->buffer);
    if ((recvrv = recv(client->socket_fd, buffer, buff_av_size - 1, 0)) == -1) {
        on_exit_client(server, client);
        return exit_error(0, "recv error : %s\n", strerror(errno));
    }
    else if (recvrv == 0) {
        on_exit_client(server, client);
        return exit_error(0, "recv error : no data\n");
    }
    return on_available_data2(server, client, recvrv, buffer);
}
