#!/usr/bin/python3

from core.GUIInterface import *
from gui.constantes import *
from random import *
from sys import *
import time
import threading

class GUI:
    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()
        self.gui_interface = GUIInterface()
        self.texture = 0
        self.map = 0
        self.window = 0
        self.playerList = PlayerList()
        self.wait_start = threading.Condition(threading.Lock())
        print("init")

    def update(self):
        with self.wait_start:
            self.wait_start.wait()
        while True:

            # Check mouse click
            print("MOUSE: ".format(pygame.mouse.get_pos()))

            self.map.display_content(self.window)
            self.playerList.display_players(self.window)
            pygame.display.flip()

    def onGameStart(self):
        pygame.init()
        pygame.display.set_caption("hello")

    #msz
    # size=(width, height)
    def onMapSize(self, size):
        self.window = pygame.display.set_mode((size[0] * 48, size[1] * 48))
        self.map = Map(size[0] * 48, size[1] * 48)
        self.map.create(self.window)
        print("onMapSize size={}".format(size))
        with self.wait_start:
            self.wait_start.notify()

    #bct
    # items: {'linemate': 0, 'deraumere': 0, 'food': 0, ...}
    def onMapCaseContent(self, pos, resources):
        #self.map.read(self.window)
        self.map.add_case_content(pos[0], pos[1], resources)
        #self.map.display_content(self.window)
        #self.playerList.display_players(self.window)
        #pygame.display.flip()
        print("onMapCaseContent pos={} resources={}".format(pos, resources))

    #tna
    def onTeamName(self, team_name):
        Teams.instance().addTeam(team_name)
        print("onTeamName team_name={}".format(team_name))

    #pnw
    def onPlayerConnect(self, player_num, pos, orientation, level, team_name):
        link = Perso(player_num, team_name, 0, self.map)
        #link.assign_model()
        link.set_direction(orientation)
        link.x = pos[0] * 48
        link.y = pos[1] * 48

        self.playerList.add_player(link)
        print("onPlayerConnect player_num={} pos={} orien={} level={} team_name={}".format(
            player_num, pos, orientation, level, team_name
        ))

    #ppo
    def onPlayerPos(self, player_num, pos, orientation):
        index = self.playerList.get_player(int(player_num))
        player = self.playerList.list[index]
        player.set_direction(orientation)
        player.x = pos[0] * 48
        player.y = pos[1] * 48

        print("onPlayerPos player_num={} pos={} orien={}".format(
            player_num, pos, orientation
        ))

    #plv
    def onPlayerLevel(self, player_num, level):
        index = self.playerList.get_player(int(player_num))
        player = self.playerList.list[index]
        player.action_previous = player.action
        player.action = player.spriteSheet['lvlUp']

        index = self.playerList.get_player(player_num)
        player = self.playerList.list[index]
        print("onPlayerLevel player_num={} level={}".format(player_num, level))

    #pin
    def onPlayerInventory(self, player_num, pos, resources):
        print("onPlayerInventory player_num={} pos={} resources={}".format(
            player_num, pos, resources
        ))

    #pex
    def onPlayerSlay(self, player_num):
        print("onPlayerSlay player_num={}".format(player_num))

    #pbc
    def onPlayerBroadcast(self, player_num, message):

        return # Cauz spam (Debug reasons)

        print("onPlayerBroadcast player_num={} message={}".format(
            player_num, message
        ))

    #pic
    def onFirstPlayerTriggerSpell(self, pos, level, players_num):
        index = self.playerList.get_player(int(player_num))
        player = self.playerList.list[index]
        player.action_previous = player.action
        player.action = player.spriteSheet['incant']
        print("onFirstPlayerTriggerSpell pos={} level={} players_num={}".format(
            pos, level, players_num
        ))

    #pie
    def onEndSpell(self, pos, result):
        player.action = player.action_previous
        print("onEndSpell pos={} result={}".format(pos, result))

    #pfk
    def onPlayerLayEgg(self, player_num):
        index = self.playerList.get_player(int(player_num))
        player = self.playerList.list[index]
        player.action_previous = player.action
        player.action = player.spriteSheet['layEgg']
        print("onPlayerLayEgg player_num={}".format(player_num))

    #pdr
    def onPlayerThrowResource(self, player_num, resource):
        print("onPlayerThrowResource player_num={} resource={}".format(
            player_num, resource
        ))

    #pgt
    def onPlayerTakeResource(self, player_num, resource):
        index = self.playerList.get_player(int(player_num))
        player = self.playerList.list[index]
        player.action_previous = player.action
        player.action = player.spriteSheet['take']

        print("onPlayerTakeResource player_num={} resource={}".format(
            player_num, resource
        ))

    #pdi
    def onPlayerDieOfHunger(self, player_num):
        index = self.playerList.get_player(int(player_num))
        player = self.playerList.list[index]
        player.action_previous = player.action
        player.action = player.spriteSheet['death']

        self.playerList.remove_player(player_num)
        print("onPlayerDieOfHunger player_num={}".format(player_num))

    #enw
    def onPlayerLaid(self, egg_num, player_num, pos):
        # TODO Spawn egg?
        # keep player team in egg

        print("onPlayerLaid egg_num={} player_num={} pos={}".format(
            egg_num, player_num, pos
        ))

    #eht
    def onEggHatch(self, egg_num):
        # TODO rm egg
        # TODO spawn player ???

        print("onEggHatch egg_num={}".format(egg_num))

    def onPlayerConnectedAfterHatch(self, egg_num):
        print("onPlayerConnectedAfterHatch egg_num={}".format(egg_num))

    #ebo
    def onEggDieOfHunger(self, egg_num):
        print("onEggDieOfHunger egg_num={}".format(egg_num))

    #edi
    def onServerTimeUnit(self, unit_time):
        print("onServerTimeUnit unit_time={}".format(unit_time))

    #sgt
    def onServerTimeUnitUpdated(self, unit_time):
        print("onServerTimeUnitUpdated unit_time={}".format(unit_time))

    #seg
    def onEndGame(self, team_name):
        print("onEndGame team_name={}".format(team_name))

    #smg
    def onServerMessage(self, message):
        print("onServerMessage message={}".format(message))

    #suc
    def onWrongCommand(self):
        print("onWrongCommand")

    #sbp
    def onWrongCommandParameters(self):
        print("onWrongCommandParameters")
