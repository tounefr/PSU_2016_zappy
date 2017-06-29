/*
** look.c for look in /home/arsene/Desktop/{EPITECH}/PSU/PSU_2016_zappy/src/server
**
** Made by arsene
** Login   <arsene@arsene-HP-EliteBook-840-G2>
**
** Started on  Mon Jun 26 14:18:29 2017 arsene
** Last update Thu Jun 29 17:02:28 2017 arsene
*/

#include <stdlib.h>
#include <string.h>
#include "server.h"

char		*get_type(int i)
{
  if (i == TYPE_FOOD)
    return ("food");
  else if (i == TYPE_LINEMATE)
    return ("linemate");
  else if (i == TYPE_DERAUMERE)
    return ("deraumere");
  else if (i == TYPE_SIBUR)
    return ("sibur");
  else if (i == TYPE_MENDIANE)
    return ("mendiane");
  else if (i == TYPE_PHIRAS)
    return ("phiras");
  else if (i == TYPE_THYSTAME)
    return ("thystame");
  else if (i == TYPE_PLAYER)
    return ("player");
  else if (i == TYPE_EGG)
    return ("egg");
}

char		*get_tiles_infos(int pos, t_server *server, char *message)
{
  int		i;
  int		count;

  count = 0;
  for (i = 0; i < RESOURCES_NBR_TYPES; i++)
    {
      if (server->map.cases[pos][i] > 0)
	{
	  while (server->map.cases[pos][i] > count)
	    {
	      if (count > 0)
		{
		  message = realloc(message, strlen(message) + 2);
		  message = strcat(message, " ");
		}
	      printf("WHAT IS ABOUT TO BE WRITTEN : %s\n", get_type(i));
	      sleep(1);

	      if (message != NULL)
		message = realloc(message, strlen(message) + strlen(get_type(i)) + 1);
	      else
		message = realloc(message, strlen(get_type(i)) + 1);
	      message = strcat(message, get_type(i));
	      count++;
	    }
	}
    }
  printf("pos : %d\n", pos);
  if (message != NULL)
    message = realloc(message, strlen(message) + 2);
  else
    message = realloc(message, 2);
  message = strcat(message, ",");
  return (message);
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
  j = 1;
  field_of_view = malloc(1);
  field_of_view = '\0';
  curr_pos = client->pos.x + (client->pos.y * server->map.height);
  if (client->orientation == ORIENT_NORTH ||
      client->orientation == ORIENT_SOUTH)
    {
      while (i <= client->level)
	{
	  if (client->orientation == ORIENT_NORTH)
	    front = curr_pos - (i * server->map.width);
	  if (client->orientation == ORIENT_SOUTH)
	    front = curr_pos + (i * server->map.width);


	  field_of_view = get_tiles_infos(front, server, field_of_view);
	  printf("FRONT\n");

	  if (i != 0)
	    {
	      while (j <= i)
		{
		  field_of_view = get_tiles_infos(front - j, server, field_of_view);
		  printf("LEFT\n");
		  field_of_view = get_tiles_infos(front + j, server, field_of_view);
		  printf("RIGHT\n");
		  j++;
		}
	    }
	  j = 1;
	  i++;
	}
    }
  else if (client->orientation == ORIENT_EAST ||
	   client->orientation == ORIENT_WEST)
    {
      while (i <= client->level)
	{
	  if (client->orientation == ORIENT_EAST)
	    front = curr_pos + i;
	  if (client->orientation == ORIENT_WEST)
	    front = curr_pos - i;

	  field_of_view = get_tiles_infos(front, server, field_of_view);

	  while (j <= client->level)
	    {
	      field_of_view = get_tiles_infos(front + (j * server->map.width)
					      , server, field_of_view);
	      field_of_view = get_tiles_infos(front - (j * server->map.width)
					      , server, field_of_view);
	      j++;
	    }
	  j = 0;
	  i++;
	}
    }
  if (field_of_view != NULL)
    {
      field_of_view[strlen(field_of_view) - 1] = '\0';
      packet_send(client, "%s", field_of_view);
    }
    }
