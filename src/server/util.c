/*
** util.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_zappy/src/server
** 
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
** 
** Started on  Fri Jun 23 15:01:31 2017 Thomas HENON
** Last update Fri Jun 23 15:01:31 2017 Thomas HENON
*/

char is_legal_network_char(char c)
{
    return (!(c >= 32 && c <= 126) &&
            c != '\n');
}
