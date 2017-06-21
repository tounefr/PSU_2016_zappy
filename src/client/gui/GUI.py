from GUIInterface import *

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
        print("onMapContent pos={} resources={}".format(pos, resources))

    #tna
    def onTeamNames(self, team_name):
        print("onTeamNames team_name={}".format(team_name))

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
        pass

    #pic
    def onFirstPlayerTriggerSpell(self, pos, level, players_num):
        pass

    #pie
    def onEndSpell(self, pos, result):
        pass

    #pfk
    def onPlayerLayEgg(self, player_name):
        pass

    #pdr
    def onPlayerThrowResource(self, player_num, resource):
        pass

    #pgt
    def onPlayerTakeResource(self, player_num, resource):
        pass

    #pdi
    def onPlayerDieOfHunger(self, player_name):
        pass

    #enw
    def onPlayerLaid(self, egg_num, player_name, pos):
        pass

    #eht
    def onEggHatch(self, egg_num):
        pass

    def onPlayerConnectedAfterHatch(self, egg_num):
        pass

    #ebo
    def onEggDieOfHunger(self, egg_num):
        pass

    #edi
    def onServerTimeUnit(self, unit_time):
        pass

    #sgt
    def onServerTimeUnitUpdated(self, unit_time):
        pass

    #seg
    def onEndGame(self, team_name):
        pass

    #smg
    def onServerMessage(self, server_message):
        pass

    #suc
    def onWrongCommand(self):
        pass

    #sbp
    def onWrongCommandParameters(self):
        pass