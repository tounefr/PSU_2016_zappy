from AIInterface import *
import time

class AI:
    def __init__(self):
        self.ai_interface = AIInterface()

    def onGameStart(self):
        print("Game start")
        print("Game map size : {}".format(self.ai_interface.getMapSize()))
        print("Team name : {}".format(self.ai_interface.getTeamName()))
        print("Turn right result : {}".format(self.ai_interface.turnRightAction()))
        print("Turn left result : {}".format(self.ai_interface.turnLeftAction()))
        print("Move forward result : {}".format(self.ai_interface.moveForwardAction()))
        print("Look Around result : {}".format(self.ai_interface.lookAroundAction()))
        print("Inventory result : {}".format(self.ai_interface.inventoryAction()))
        print("Broadcast result : {}".format(self.ai_interface.broadcastAction("salut tout le monde")))
        print("numberOfTeamSlotsUnusedAction result : {}".format(self.ai_interface.numberOfTeamSlotsUnusedAction()))
        print("fork result : {}".format(self.ai_interface.forkAction()))
#       bugged
#        print("ejectPlayerTileAction result : {}".format(self.ai_interface.ejectPlayerTileAction()))
        print("takeObjectAction result : {}".format(self.ai_interface.takeObjectAction("food")))
        print("setObjectDownAction result : {}".format(self.ai_interface.setObjectDownAction("food")))
#       bugged
#        print("startIncantationAction result : {}".format(self.ai_interface.startIncantationAction()))

    def onPlayerEject(self, res):
        print("onPlayerEject res={}".format(res))

    def onPlayerDead(self, status):
        print("onPlayerDead")

    def onIncantation(self, status):
        if type(status) is int:
            print("Level up : {}".format(status))
        elif status == "underway":
            print("Underway")
        elif status == "ko":
            print("Incantation failed")

    def onMessage(self, msg):
        print("onMessage: {}".format(msg))

    def onNbrOfTeamSlotsUnused(self, count):
        print(count)