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
#        self.MsgQueue = queue.Queue()
        pass

    @staticmethod
    def on_game_start():
        print("Game start")
#        AIInterface.instance().turnRight()
#        AIInterface.instance().turnLeft()
        AIInterface.instance().lookAroundAction()

    @staticmethod
    def onMovement():
        print("onMovement")
#        AIInterface.instance().lookAroundAction()

    @staticmethod
    def onTurn(direction):
        print("onTurn dir={}".format(direction))

    @staticmethod
    def onLookAroundResult(items):
        print("onLookAroundResult")
        print(items)
        nb = len(items[0]) - 1
        for i in range(0, nb):
            AIInterface.instance().takeObjectAction()

    @staticmethod
    def onInventoryContent(inventory):
        print("onInventoryContent")
        print(inventory)

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
    def onIncantationFinished():
        pass
