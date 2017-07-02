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

LDFLAGS+=
CFLAGS+= -I./includes -W -Wall -fPIC

SERVER_NAME = zappy_server

SERVER_SRCS =   src/server/callback.c \
                src/server/client.c \
                src/server/commands.c \
                src/server/commands2.c \
                src/server/commands3.c \
                src/server/cycle.c \
                src/server/egg.c \
                src/server/eject.c \
                src/server/game.c \
                src/server/globals.c \
                src/server/gui.c \
                src/server/incantation.c \
                src/server/look.c \
                src/server/look2.c \
                src/server/look3.c \
                src/server/look4.c \
                src/server/main.c \
                src/server/map.c \
                src/server/opts.c \
                src/server/packet.c \
                src/server/packet2.c \
                src/server/player.c \
                src/server/resources.c \
                src/server/select.c \
                src/server/server.c \
                src/server/team.c \
                src/server/update.c \
                src/server/util.c \
                src/server/util2.c \
                src/common/error.c \
                src/common/generic_list.c \
                src/common/generic_list2.c \
                src/common/util.c \
                src/libnetwork/packet.c \
                src/libnetwork/socket.c \
                src/libnetwork/socket2.c \
                src/libnetwork/socket_server.c

SERVER_OBJS = $(SERVER_SRCS:.c=.o)

LIBNETWORK_NAME = libnetwork.so
LIBNETWORK_SRCS =   src/libnetwork/packet.c \
                    src/libnetwork/socket.c \
                    src/libnetwork/socket2.c \
                    src/libnetwork/socket_server.c \
                    src/common/error.c \
                    src/common/generic_list.c \
                    src/common/generic_list2.c \
                    src/common/util.c

LIBNETWORK_OBJS = $(LIBNETWORK_SRCS:.c=.o)

AI_NAME = zappy_ai

all: libnetwork zappy_server zappy_ai_package

libnetwork: $(LIBNETWORK_OBJS)
	$(CC) -fPIC -shared -o $(LIBNETWORK_NAME) $(LIBNETWORK_OBJS)

zappy_ai_package: zappy_ai
	sudo pyinstaller -y --distpath ./ -n zappy_ai -F ./src/client/ZappyClient.py

zappy_ai:
	sudo apt-get install python3 python3-pip python3-dev -y
	sudo pip3 install -r requirements.txt

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
