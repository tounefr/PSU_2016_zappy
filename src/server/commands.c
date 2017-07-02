/*
** commands.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Fri Jun 23 15:00:43 2017 Thomas HENON
** Last update Sun Jul  2 17:04:47 2017 arsene
*/

#include "server.h"

char    onSetObjectPacket(t_server *server, t_client *client, char *packet)
{
    int i;
    char food[100];
    int client_pos;
    t_callback *callback;

    memset((char*)&food, 0, sizeof(food));
    strncpy((char*)&food, packet + 5, sizeof(food) - 1);
    client_pos = client->pos.x + client->pos.y * server->map.width;
    for (i = 0; i < RESOURCES_NBR_TYPES; i++) {
        if ((!is_stone(i) && strcmp((char*)&food, "food")) ||
                strcmp(get_g_foods()[i].s, (char*)&food))
            continue;
        if (client->inventory[get_g_foods()[i].type] - 1 < 0)
            return packet_send(client, "ko\n");
        client->inventory[get_g_foods()[i].type]--;
        server->map.cases[client_pos][get_g_foods()[i].type]++;
        send_gui_packet(server, "pdr %d %d\n",
                        client->num, get_g_foods()[i].type);
        if (get_g_foods()[i].type == TYPE_FOOD &&
            (callback = get_callback(client, onPlayerDead)))
            callback->cycles -= CYCLES_PER_LIFE_UNIT;
        gui_send_map_case(server, client->pos.x, client->pos.y);
        return packet_send(client, "ok\n");
    }
    return packet_send(client, "ko\n");
}


char    onTakeObjectPacket(t_server *server, t_client *cli, char *packet)
{
  int i;
  char food[100];
  int client_pos;
  t_callback *cb;

  memset(&food, 0, sizeof(food));
  strncpy((char*)&food, packet + 5, sizeof(food) - 1);
  client_pos = cli->pos.x + cli->pos.y * server->map.width;
  for (i = 0; i < RESOURCES_NBR_TYPES; i++)
    {
      if ((!is_stone(i) && strcmp((char*)&food, "food")) ||
	  strcmp(get_g_foods()[i].s, (char*)&food))
	continue;
      if (server->map.cases[client_pos][get_g_foods()[i].type] - 1 < 0)
	return packet_send(cli, "ko\n");
      cli->inventory[get_g_foods()[i].type]++;
      take_ressource(server, client_pos, i);
      send_gui_packet(server, "pgt %d %d\n", cli->num, get_g_foods()[i].type);
      if (get_g_foods()[i].type == TYPE_FOOD &&
	  (cb = get_callback(cli, onPlayerDead)))
	cb->cycles += CYCLES_PER_LIFE_UNIT;
      gui_send_map_case(server, cli->pos.x, cli->pos.y);
      return packet_send(cli, "ok\n");
    }
  return packet_send(cli, "ko\n");
}

char    onPreForkPacket(t_server *server, t_client *client, char *packet)
{
    (void)packet;
    send_gui_packet(server, "pfk %d\n", client->num);
    return 1;
}

char    onPostForkPacket(t_server *server, t_client *client, char *packet)
{
    (void)packet;
    if (!lay_egg(server, client))
        return packet_send(client, "ko\n");
    return packet_send(client, "ok\n");
}
