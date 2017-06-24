#!/usr/bin/python3

#from GUIInterface import *

class GUI:
    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()
        self.gui_interface = GUIInterface()

    def onGameStart(self):
        print("gui")

    #msz
    # size=(width, height)
    def onMapSize(self, size):
        print("onMapSize size={}".format(size))

    #bct
    # items: {'linemate': 0, 'deraumere': 0, 'food': 0, ...}
    def onMapCaseContent(self, pos, resources):
        print("onMapCaseContent pos={} resources={}".format(pos, resources))

    #tna
    def onTeamName(self, team_name):
        print("onTeamName team_name={}".format(team_name))

    #pnw
    def onPlayerConnect(self, player_num, pos, orientation, level, team_name):
        print("onPlayerConnect player_num={} pos={} orien={} level={} team_name={}".format(
            player_num, pos, orientation, level, team_name
        ))

    #ppo
    def onPlayerPos(self, player_num, pos, orientation):
        print("onPlayerPos player_num={} pos={} orien={}".format(
            player_num, pos, orientation
        ))

    #plv
    def onPlayerLevel(self, player_num, level):
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
        print("onPlayerBroadcast player_num={} message={}".format(
            player_num, message
        ))

    #pic
    def onFirstPlayerTriggerSpell(self, pos, level, players_num):
        print("onFirstPlayerTriggerSpell pos={} level={} players_num={}".format(
            pos, level, players_num
        ))

    #pie
    def onEndSpell(self, pos, result):
        print("onEndSpell pos={} result={}".format(pos, result))

    #pfk
    def onPlayerLayEgg(self, player_num):
        print("onPlayerLayEgg player_num={}".format(player_num))

    #pdr
    def onPlayerThrowResource(self, player_num, resource):
        print("onPlayerThrowResource player_num={} resource={}".format(
            player_num, resource
        ))

    #pgt
    def onPlayerTakeResource(self, player_num, resource):
        print("onPlayerTakeResource player_num={} resource={}".format(
            player_num, resource
        ))

    #pdi
    def onPlayerDieOfHunger(self, player_num):
        print("onPlayerDieOfHunger player_num={}".format(player_num))

    #enw
    def onPlayerLaid(self, egg_num, player_num, pos):
        print("onPlayerLaid egg_num={} player_num={} pos={}".format(
            egg_num, player_num, pos
        ))

    #eht
    def onEggHatch(self, egg_num):
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
