/*
** look.c for look in /home/arsene/Desktop/{EPITECH}/PSU/PSU_2016_zappy/src/server
**
** Made by arsene
** Login   <arsene@arsene-HP-EliteBook-840-G2>
**
** Started on  Mon Jun 26 14:18:29 2017 arsene
** Last update Wed Jun 28 15:55:42 2017 arsene
*/

#include "server.h"

char		*get_tiles_infos(int pos, t_server *server)
{
  int		i;

  printf("%s\n", server->map.cases[pos][get_g_foods()[i].s]);
  /* char		*buffer; */
  /* int		i; */
  /* int		count_buffer; */

  /* count_buffer = 0; */
  /* for (i = 0; i < RESOURCES_NBR_TYPES; i++) */
  /*   { */
  /*     if (server->map.cases[pos][get_g_foods()[i].type] > 0) */
  /* 	{ */
  /* 	  while (count_buffer < ) */
  /* 	} */
  /*   } */
}

char		*look(t_client *client, t_server *server)
{
  char		*field_of_view;
  int		vision;
  int		i;
  int		j;
  int		curr_pos;
  int		front;

  i = 0;
  j = 0;
  vision = 0;
  printf("/!\\ LOOK FUNCTION\n /!\\\n");
  printf("/!\\ LOOK FUNCTION\n /!\\\n");
  printf("/!\\ LOOK FUNCTION\n /!\\\n");
  curr_pos = client->pos.x + (client->pos.y * server->map.height);
  if (client->orientation == ORIENT_NORTH ||
      client->orientation == ORIENT_SOUTH)
    {
      while (i < client->level)
	{
	  if (client->orientation == ORIENT_NORTH)
	    front = server->map.cases[curr_pos - (i * server->map.width)];
	  if (client->orientation == ORIENT_SOUTH)
	    front = server->map.cases[curr_pos + (i * server->map.width)];
	  get_tiles_infos(front, server);
	  while (j < client->level)
	    {
	      get_tiles_infos(front + j, server);
	      get_tiles_infos(front - j, server);
	      j++;
	    }
	  j = 0;
	}
      i++;
    }
  else if (client->orientation == ORIENT_EAST ||
	   client->orientation == ORIENT_WEST)
    {
      while (i < client->level)
	{
	  if (client->orientation == ORIENT_EAST)
	    front = server->map.cases[curr_pos + i];
	  if (client->orientation == ORIENT_WEST)
	    front = server->map.cases[curr_pos - i];
	  get_tiles_infos(front, server);
	  while (j < client->level)
	    {
	      get_tiles_infos(front + (j * server->map.width), server);
	      get_tiles_infos(front - (j * server->map.width), server);
	      j++;
	    }
	  j = 0;
	}
      i++;
    }
}
