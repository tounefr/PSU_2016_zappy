##
## Makefile for  in /home/toune/Documents/Epitech/projets/PSU_2016_myftp
## 
## Made by Thomas HENON
## Login   <thomas.henon@epitech.eu>
## 
## Started on  Thu May 18 10:29:51 2017 Thomas HENON
## Last update Tue Jun 27 18:42:38 2017 
##

CC = gcc

LDFLAGS+= -g
CFLAGS+= -I./includes -W -Wall -fPIC -g

SERVER_NAME = zappy_server
SERVER_SRCS = $(wildcard src/server/*.c) \
              $(wildcard src/common/*.c) \
              $(wildcard src/libnetwork/*.c)
SERVER_OBJS = $(SERVER_SRCS:.c=.o)

LIBNETWORK_NAME = libnetwork.so
LIBNETWORK_SRCS = $(wildcard src/common/*.c \
		          $(wildcard src/libnetwork/*.c))
LIBNETWORK_OBJS = $(LIBNETWORK_SRCS:.c=.o)

AI_NAME = zappy_ai

all: libnetwork zappy_server zappy_ai

libnetwork: $(LIBNETWORK_OBJS)
	$(CC) -fPIC -shared -o $(LIBNETWORK_NAME) $(LIBNETWORK_OBJS)

zappy_ai:
	sudo pip3 install -r requirements.txt
	sudo pyinstaller -y --distpath ./ -n zappy_ai -F ./src/client/ZappyClient.py

zappy_server: $(SERVER_OBJS)
	$(CC) -o $(SERVER_NAME) $(SERVER_OBJS) $(LDFLAGS)

clean:
	$(RM) $(SERVER_OBJS)
	$(RM) $(LIBNETWORK_OBJS)

fclean: clean
	$(RM) $(SERVER_NAME)
	$(RM) $(LIBNETWORK_NAME)
	$(RM) $(AI_NAME)

re: fclean all

.PHONY: all clean fclean re zappy_ai zappy_server
