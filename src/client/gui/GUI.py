from GUIInterface import *

class GUI:
    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()
        self.gui_interface = GUIInterface()

    def onGameStart(self):
        print("gui")

    #msz
    def onMapSize(self, b):
        print(b)
#        print("mapsize: {}".format(sizes))

    #bct
    # items: {'linemate': 0, 'deraumere': 0, 'food': 0, ...}
    def onMapContent(self, pos, resources):
        pass

    #tna
    def onTeamNames(self, team_name):
        pass

    #pnw
    def onPlayerConnect(self, player_name, pos, orientation, level, team_name):
        pass

    #ppo
    def onPlayerPos(self, player_name, pos, orientation):
        pass

    #plv
    def onPlayerLevel(self, player_name, level):
        pass

    #pin
    def onPlayerInventory(self, player_name, pos, items):
        pass

    #pex
    def onPlayerSlay(self, player_name):
        pass

    #pbc
    def onPlayerBroadcast(self, player_name, message):
        pass

    #pic
    def onFirstPlayerTriggerSpell(self, pos, level, player_names):
        pass

    #pie
    def onEndSpell(self, pos, result):
        pass

    #pfk
    def onPlayerLayEgg(self, player_name):
        pass

    #pdr
    def onPlayerThrowResource(self, player_name, resource_num):
        pass

    #pgt
    def onPlayerTakeResource(self, player_name, resource_num):
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