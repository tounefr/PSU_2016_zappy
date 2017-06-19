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

    @staticmethod
    def onTurn(direction):
        print("onTurn dir={}".format(direction))
        AIInterface.instance().inventoryAction()
        AIInterface.instance().lookAroundAction()
        AIInterface.instance().takeObjectAction()
        AIInterface.instance().setObjectDownAction()
#        AIInterface.instance().setObjectDownAction()
#        AIInterface.instance().startIncantationAction()

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
#        AIInterface.instance().broadcastAction("Hello")

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
    # status peut être égale à ko ou "underway" ou le level sur un int
    def onIncantation(status):
        if type(status) is int:
            print("Level up : {}".format(status))
        elif status == "underway":
            print("Underway")
        elif status == "ko":
            print("Incantation failed")

    @staticmethod
    def onBroadcast():
        pass

    @staticmethod
    def onMessage(i, msg):
        print(msg)
