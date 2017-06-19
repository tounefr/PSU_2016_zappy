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
        AIInterface.instance().turnLeftAction()

    @staticmethod
    def onMovement():
        print("onMovement")

    @staticmethod
    def onTurn(direction):
        print("onTurn dir={}".format(direction))
        AIInterface.instance().inventoryAction()

    @staticmethod
    def onLookAroundResult(items):
        print("onLookAroundResult")
        print(items)

    @staticmethod
    def onInventoryContent(inventory):
        print("onInventoryContent")
        print(inventory)
        AIInterface.instance().broadcastAction("Hello")

    @staticmethod
    def onPlayerForked():
        print("Forked")

    @staticmethod
    def onPlayerEject(res):
        print("onPlayerEject res={}".format(res))

    @staticmethod
    def onPlayerDead():
        print("onPlayerDead")

    @staticmethod
    def onTakeObject(res):
        print("onTakeObject res={}".format(res))

    @staticmethod
    def onObjectDown(res):
        print("onObjectDown res={}".format(res))

    @staticmethod
    def onIncantation():
        pass

    @staticmethod
    def onBroadcast():
        pass

    @staticmethod
    def onMessage(i, msg):
        print(msg)
