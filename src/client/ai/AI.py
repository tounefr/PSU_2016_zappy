from AIInterface import *
import queue

class AI:

    g_instance = None

    @staticmethod
    def instance():
        if AI.g_instance is None:
            AI.g_instance = AI()
        return AI.g_instance

    def __init__(self):
        pass

    @staticmethod
    def on_game_start():
        print("Game start")
        print("Turn right result : {}".format(AIInterface.instance().turnRightAction()))
        print("Turn left result : {}".format(AIInterface.instance().turnLeftAction()))
        print("Move forward result : {}".format(AIInterface.instance().moveForwardAction()))
        print("Look Around result : {}".format(AIInterface.instance().lookAroundAction()))
        print("Inventory result : {}".format(AIInterface.instance().inventoryAction()))
        print("Broadcast result : {}".format(AIInterface.instance().broadcastAction("salut tout le monde")))
        print("numberOfTeamSlotsUnusedAction result : {}".format(AIInterface.instance().numberOfTeamSlotsUnusedAction()))
        print("fork result : {}".format(AIInterface.instance().forkAction()))
        print("ejectPlayerTileAction result : {}".format(AIInterface.instance().ejectPlayerTileAction()))
        print("takeObjectAction result : {}".format(AIInterface.instance().takeObjectAction("food")))
        print("setObjectDownAction result : {}".format(AIInterface.instance().setObjectDownAction("food")))
#        print("startIncantationAction result : {}".format(AIInterface.instance().startIncantationAction()))

    @staticmethod
    def onPlayerEject(res):
        print("onPlayerEject res={}".format(res))

    @staticmethod
    def onPlayerDead():
        print("onPlayerDead")

    @staticmethod
    def onIncantation(status):
        if type(status) is int:
            print("Level up : {}".format(status))
        elif status == "underway":
            print("Underway")
        elif status == "ko":
            print("Incantation failed")

    @staticmethod
    def onMessage(i, msg):
        print("onMessage: {}".format(msg))

    @staticmethod
    def onNbrOfTeamSlotsUnused(count):
        print(count)