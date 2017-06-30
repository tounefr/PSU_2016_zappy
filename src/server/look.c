/*
** look.c for look in /home/arsene/Desktop/{EPITECH}/PSU/PSU_2016_zappy/src/server
**
** Made by arsene
** Login   <arsene@arsene-HP-EliteBook-840-G2>
**
** Started on  Mon Jun 26 14:18:29 2017 arsene
** Last update Fri Jun 30 17:22:29 2017 arsene
*/

#include <stdlib.h>
#include <string.h>
#include "server.h"


typedef struct	s_cell
{
  int		content[9];
}		t_cell;

typedef struct	s_look
{
  t_cell	cell[64];
}		t_look;

int	coordsToIndex(t_server *server, t_pos pos)
{
  printf("Looking at coords: [%i; %i]\n", pos.x, pos.y);
  while (pos.x <= 0)
    pos.x += server->map.width;
  while (pos.x > server->map.width)
    pos.x -= server->map.width;
  while (pos.y <= 0)
    pos.y += server->map.height;
  while (pos.y > server->map.height)
    pos.y -= server->map.height;
  printf("Giving: [%i; %i] ->%i\n\n", pos.x, pos.y, (pos.y * server->map.width) + pos.x);
  return ((pos.y * server->map.width) + pos.x);
}

void	init_look(t_look *tmp)
{
  int	i;
  int	j;

  i = 0;
  while (i < 64)
    {
      j = 0;
      while (j < 9)
	{
	  tmp->cell[i].content[j] = 0;
	  j++;
	}
      i++;
    }
}

void	get_ressources(t_server *s, t_look *see, int index, int pos)
{
  int	i;

  i = 0;
  while (i < 9)
    {
      see->cell[index].content[i] = s->map.cases[pos][i];
      i++;
    }
}

void	lookUp(t_server *s, t_client *c, t_look *see)
{
  t_pos	target;
  t_pos	tmp;
  int	range;
  int	index;
  int	offset;

  range = 0;
  index = 0;
  target = c->pos;
  while (range < 8)
    {
      tmp = target;
      tmp.x -= range;
      while (tmp.x <= target.x + range)
	{
	  get_ressources(s, see, index, coordsToIndex(s, tmp));
	  tmp.x++;
	  index++;
	}
      target.y--;
      range++;
    }
}

void    lookDown(t_server *s, t_client *c, t_look *see)
{
  t_pos target;
  t_pos tmp;
  int   range;
  int   index;
  int   offset;

  range = 0;
  index = 0;
  target = c->pos;
  while (range < 8)
    {
      tmp = target;
      tmp.x += range;
      while (tmp.x >= target.x - range)
	{
	  get_ressources(s, see, index, coordsToIndex(s, tmp));
	  tmp.x--;
	  index++;
	}
      target.y++;
      range++;
    }
}

void    lookLeft(t_server *s, t_client *c, t_look *see)
{
  t_pos target;
  t_pos tmp;
  int   range;
  int   index;

  range = 0;
  index = 0;
  target = c->pos;
  while (range < 8)
    {
      tmp = target;
      tmp.y += range;
      while (tmp.y >= target.y - range)
	{
	  get_ressources(s, see, index, coordsToIndex(s, tmp));
	  tmp.y--;
	  index++;
	}
      target.x--;
      range++;
    }
}

void    lookRight(t_server *s, t_client *c, t_look *see)
{
  t_pos target;
  t_pos tmp;
  int   range;
  int   index;

  range = 0;
  index = 0;
  target = c->pos;
  while (range < 8)
    {
      tmp = target;
      tmp.y -= range;
      while (tmp.y <= target.y + range)
	{
	  get_ressources(s, see, index, coordsToIndex(s, tmp));
	  tmp.y++;
	  index++;
	}
      target.x++;
      range++;
    }
}

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
  /*
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
  */
  return (NULL);
}

char	*myAppend(char *old, char *str)
{
  char	*new;
  int	size;

  new = NULL;
  size = strlen(old) + strlen(str);
  if ((new = malloc((size + 1) * sizeof(char))) == NULL)
    return (new);
  new[0] = '\0';
  strcat(new, old);
  strcat(new, str);
  new[size] = '\0';
  if (old != NULL)
    free(old);
  return (new);
}

void	convertView(t_client *c, t_look *see)
{
  char	*buffer;
  int	limit;
  int	index;
  int	i;
  int	x;
  int	first;

  i = 0;
  limit = 1;
  while (i < c->level)
    {
      limit += limit + 2;
      i++;
    }
  printf("### [LOOK] index of view [0, %i]\n", limit - 1);

  index = 0;
  if ((buffer = malloc(1)) == NULL)
    return;
  buffer[0] = 0;
  buffer = myAppend(buffer, "[");
  while (index < limit)
    {
      if (index != 0)
	buffer = myAppend(buffer, ",");
      i = 0;
      first = 1;
      for (i = 0; i < 9; i++)
	{
	  x = 0;
	  while (x < see->cell[index].content[i])
	    {
	      if (first != 1)
		buffer = myAppend(buffer, " ");
	      first = 0;
	      buffer = myAppend(buffer, get_type(i));
	      x++;
	    }
	}
      index++;
    }
  buffer = myAppend(buffer, "]");
  printf("### [LOOK] Goind to send: \"%s\"\n", buffer);
  packet_send(c, "%s\n", buffer);
}

void	debug_count(t_server *s)
{
  int  	total;
  int  	i;
  int	j;

  i = 0;
  total = 0;
  printf("Counting ressources...\n");
  while (i < s->map.width * s->map.height)
    {
      j = 0;
      while (j < 9)
	{
	  total += s->map.cases[i][j];
	  j++;
	}
      i++;
    }
  printf("Nb of ressources found on the map: %i\n", total);
}

char		*look(t_client *client, t_server *server)
{
  char		*field_of_view;
  int		vision;
  int		i;
  int		j;
  int		curr_pos;
  int		front;

  t_look	see;

  init_look(&see);
  printf("### START LOOK\n");
  debug_count(server);
  printf("### [DEBUG] Map %i x %i\n", server->map.width, server->map.height);
  if (client->orientation == ORIENT_NORTH)
    lookUp(server, client, &see);
  if (client->orientation == ORIENT_SOUTH)
    lookDown(server, client, &see);
  if (client->orientation == ORIENT_EAST)
    lookRight(server, client, &see);
  if (client->orientation == ORIENT_WEST)
    lookLeft(server, client, &see);
  convertView(client, &see);
  printf("### END LOOK\n");




  /*
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
  */

  char	*tmp;
  tmp = NULL;
  return (tmp);
}
