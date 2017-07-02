#!/usr/bin/python3

from core.GUIInterface import *
from gui.constantes import *
from sys import *
import time
import threading
import random

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
        t0 = time.time()
        is_displayed = False

        #pygame.mixer.music.load("src/client/gui/assets/ZappySong.mp3")
        #pygame.mixer.music.play(-1)

        score = Scoreboard.instance()
        score.setSurface(self.window)
        score.setResource()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score.UpdateMouse(True)
                elif event.type == pygame.MOUSEBUTTONUP:
                    score.UpdateMouse(False)

            if round(time.time() - t0, 1) == 0.6:
                t0 = time.time()
                is_displayed = True

            self.map.display_content(self.window)
            self.playerList.display_players(self.window, t0, is_displayed)
            score.DrawScoreboard()
            pygame.display.flip()

            is_displayed = False
            time.sleep(0.01)

    def onGameStart(self):
        pygame.init()
        pygame.display.set_caption("hello")

    #msz
    # size=(width, height)
    def onMapSize(self, size):
        Constantes.instance().setScale(size[1])
        Constantes.instance().MapWidth = size[0]
        Constantes.instance().MapHeight = size[1]
        Scoreboard.instance().setOrigin()
        self.window = pygame.display.set_mode((size[0] * Constantes.instance().tileScale + 300, size[1] * Constantes.instance().tileScale))
        self.map = Map(size[0] * Constantes.instance().tileScale, size[1] * Constantes.instance().tileScale)
        self.map.create(self.window)
        Scoreboard.instance().setMap(self.map)
        print("onMapSize size={}".format(size))
        with self.wait_start:
            self.wait_start.notify()

    #bct
    # items: {'linemate': 0, 'deraumere': 0, 'food': 0, ...}
    def onMapCaseContent(self, pos, resources):
        try:
            self.map.add_case_content(pos[0], pos[1], resources)
        except AttributeError:
            return
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
        link.x = pos[0] * Constantes.instance().tileScale
        link.y = pos[1] * Constantes.instance().tileScale

        self.playerList.add_player(link)
        print("onPlayerConnect player_num={} pos={} orien={} level={} team_name={}".format(
            player_num, pos, orientation, level, team_name
        ))

    #ppo
    def onPlayerPos(self, player_num, pos, orientation):
        try:
            index = self.playerList.get_player(int(player_num))
            player = self.playerList.list[index]
        except IndexError:
            return
        player.set_direction(orientation)
        player.x = pos[0] * Constantes.instance().tileScale
        player.y = pos[1] * Constantes.instance().tileScale

        print("onPlayerPos player_num={} pos={} orien={}".format(
            player_num, pos, orientation
        ))

    #plv
    def onPlayerLevel(self, player_num, level):
        try:
            index = self.playerList.get_player(int(player_num))
            player = self.playerList.list[index]
        except IndexError:
            return
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
        for num in players_num:
            index = self.playerList.get_player(num)
            player = self.playerList.list[index]
            player.action_previous = player.action
            player.action = player.spriteSheet['incant']
        print("onFirstPlayerTriggerSpell pos={} level={} players_num={}".format(
            pos, level, players_num
        ))

    #pie
    def onEndSpell(self, pos, result):
        #player.action = player.action_previous
        print("onEndSpell pos={} result={}".format(pos, result))

    #pfk
    def onPlayerLayEgg(self, player_num):
        try:
            index = self.playerList.get_player(int(player_num))
            player = self.playerList.list[index]
        except IndexError:
            return
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
        try:
            index = self.playerList.get_player(int(player_num))
            player = self.playerList.list[index]
        except IndexError:
            return
        player.action_previous = player.action
        player.action = player.spriteSheet['take']

        print("onPlayerTakeResource player_num={} resource={}".format(
            player_num, resource
        ))

    #pdi
    def onPlayerDieOfHunger(self, player_num):
        try:
            index = self.playerList.get_player(int(player_num))
            player = self.playerList.list[index]
        except IndexError:
            return
        player.action_previous = player.action
        player.action = player.spriteSheet['death']
        self.playerList.remove_player(player_num)

    #enw
    def onPlayerLaid(self, egg_num, player_num, pos):
        try:
            index = self.playerList.get_player(int(player_num))
            player = self.playerList.list[index]
        except IndexError:
            return
        baby_link = Perso(egg_num, player.team, 0, self.map)
        baby_link.is_egg = True
        baby_link.x = pos[0] * Constantes.instance().tileScale
        baby_link.y = pos[1] * Constantes.instance().tileScale
        baby_link.set_direction(1)
        self.playerList.add_player(baby_link)

        print("onPlayerLaid egg_num={} player_num={} pos={}".format(
            egg_num, player_num, pos
        ))

    #eht
    def onEggHatch(self, egg_num):
        try:
            index = self.playerList.get_player(int(egg_num))
            player = self.playerList.list[index]
        except IndexError:
            return
        player.set_direction(random.randint(1, 4))
        player.is_egg = False
        player.action_previous = player.action
        player.action = player.spriteSheet['hatch']
        print("onEggHatch egg_num={}".format(egg_num))

    def onPlayerConnectedAfterHatch(self, egg_num):
        print("onPlayerConnectedAfterHatch egg_num={}".format(egg_num))

    #ebo
    def onEggDieOfHunger(self, egg_num):
        try:
            index = self.playerList.get_player(int(egg_num))
            player = self.playerList.list[index]
        except IndexError:
            return
        self.playerList.remove_player(player)
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
