/*
** error.c for  in /home/toune/Documents/Epitech/projets/PSU_2016_myftp
**
** Made by Thomas HENON
** Login   <thomas.henon@epitech.eu>
**
** Started on  Thu May 18 10:27:33 2017 Thomas HENON
** Last update Thu May 18 10:27:34 2017 Thomas HENON
*/

#include "util.h"

char
exit_error(char returnv,
           char *format,
           ...)
{
    va_list args;

    va_start(args, format);
    vfprintf(stderr, format, args);
    va_end(args);
    return returnv;
}

char*
exit_ptr_error(char *returnv,
               char *format,
               ...)
{
    va_list args;
    va_start(args, format);
    fprintf(stderr, format, args);
    va_end(args);
    return returnv;
}

void
malloc_error()
{
    fprintf(stderr, "malloc error\n");
    exit(1);
}
