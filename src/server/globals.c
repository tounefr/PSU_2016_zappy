/*
** globals.c for globals in /home/arsene/Desktop/{EPITECH}/PSU/PSU_2016_zappy/src/server
**
** Made by arsene
** Login   <arsene@arsene-HP-EliteBook-840-G2>
**
** Started on  Tue Jun 27 11:19:54 2017 arsene
** Last update Tue Jun 27 17:34:47 2017 arsene
*/

#include "server.h"

t_food				*get_g_foods()
{
  static t_food			g_foods[RESOURCES_NBR_TYPES] =
    {
      { "food", TYPE_FOOD },
      { "thystame", TYPE_THYSTAME },
      { "phiras", TYPE_PHIRAS },
      { "mendiane", TYPE_MENDIANE },
      { "sibur", TYPE_SIBUR },
      { "deraumere", TYPE_DERAUMERE },
      { "linemate", TYPE_LINEMATE },
      { "player", TYPE_PLAYER },
      { "egg", TYPE_EGG }
    };
  return (g_foods);
}

t_incantation			*get_g_incantations()
{
  static t_incantation		g_incantations[NBR_LEVELS] =
    {
      { 1, { 0, 1, 0, 0, 0, 0, 0 } },
      { 2, { 0, 1, 1, 1, 0, 0, 0 } },
      { 2, { 0, 2, 0, 1, 0, 2, 0 } },
      { 4, { 0, 1, 1, 2, 0, 1, 0 } },
      { 4, { 0, 1, 2, 1, 3, 0, 0 } },
      { 6, { 0, 1, 2, 3, 0, 1, 0 } },
      { 6, { 0, 2, 2, 2, 2, 2, 1 } }
    };
  return (g_incantations);
}

t_network_commands		*g_network_commands()
{
  static t_network_commands	g_network_commands[N_NETWORK_COMMANDS] =
    {
      { "Forward", NULL, onForwardPacket, 7, FLAG_NONE },
      { "Right", NULL, onRightPacket, 7, FLAG_NONE },
      { "Left", NULL, onLeftPacket, 7, FLAG_NONE },
      { "Look", NULL, onLookPacket, 7, FLAG_NONE },
      { "Inventory", NULL, onInventoryPacket, 1, FLAG_NONE },
      { "Broadcast", NULL, onBroadcastPacket, 7, FLAG_NONE },
      { "Connect_nbr", NULL, onConnectNbrPacket, 0, FLAG_NONE },
      { "Fork", onPreForkPacket, onPostForkPacket, 42, FLAG_NONE },
      { "Eject", NULL, onEjectPacket, 7, FLAG_NONE },
      { "Take", NULL, onTakeObjectPacket, 7, FLAG_NONE },
      { "Set", NULL, onSetObjectPacket, 7, FLAG_NONE },
      { "Incantation", onPreIncantPacket, onPostIncantPacket, 300, FLAG_NONE }
    };
  return (g_network_commands);
}
