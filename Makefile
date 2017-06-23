##
## Makefile for  in /home/toune/Documents/Epitech/projets/PSU_2016_myftp
## 
## Made by Thomas HENON
## Login   <thomas.henon@epitech.eu>
## 
## Started on  Thu May 18 10:29:51 2017 Thomas HENON
## Last update Tue Jun 20 11:12:06 2017 arsene
##

CC = gcc

RM = rm -f

LDFLAGS+= -W -Wall
CFLAGS+= -I./includes -W -Wall -fPIC

CLIENT_NAME = zappy_ai
CLIENT_SRCS = $(wildcard src/client/*.c) \
              $(wildcard src/common/*.c)
CLIENT_OBJS = $(CLIENT_SRCS:.c=.o)

SERVER_NAME = zappy_server
SERVER_SRCS = $(wildcard src/server/*.c) \
              $(wildcard src/common/*.c) \
              $(wildcard src/libnetwork/*.c)
SERVER_OBJS = $(SERVER_SRCS:.c=.o)

LIBNETWORK_NAME = libnetwork.so
LIBNETWORK_SRCS = $(wildcard src/common/*.c \
		          $(wildcard src/libnetwork/*.c))
LIBNETWORK_OBJS = $(LIBNETWORK_SRCS:.c=.o)

all: libnetwork zappy_server

libnetwork: $(LIBNETWORK_OBJS)
	$(CC) -fPIC -shared -o $(LIBNETWORK_NAME) $(LIBNETWORK_OBJS)

zappy_ai: $(CLIENT_OBJS)
	$(CC) -o $(CLIENT_NAME) $(CLIENT_OBJS) $(LDFLAGS)

zappy_server: $(SERVER_OBJS)
	$(CC) -o $(SERVER_NAME) $(SERVER_OBJS) $(LDFLAGS)

clean:
	$(RM) $(SERVER_OBJS)
	$(RM) $(CLIENT_OBJS)
	$(RM) $(LIBNETWORK_OBJS)

fclean: clean
	$(RM) $(SERVER_NAME)
	$(RM) $(CLIENT_NAME)
	$(RM) $(LIBNETWORK_NAME)

re: fclean all

.PHONY: all clean fclean re zappy_ai zappy_server
