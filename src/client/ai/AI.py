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
        tiles = AIInterface.instance().lookAroundAction()
        # prendre toutes les resources sur la case
        for item in tiles[0]:
            if item == "player":
                continue
            AIInterface.instance().takeObjectAction(item)
        print(AIInterface.instance().lookAroundAction()[0])
        print(AIInterface.instance().inventoryAction())
        print(AIInterface.instance().moveForwardAction())
#        print(AIInterface.instance().turnLeftAction())

    @staticmethod
    def onMovement():
        print("onMovement")
        AIInterface.instance().lookAroundAction()

    @staticmethod
    def onTurn(direction):
        print("onTurn dir={}".format(direction))
        """
#        AIInterface.instance().inventoryAction()
        AIInterface.instance().numberOfTeamSlotsUnusedAction()
        AIInterface.instance().lookAroundAction()
        AIInterface.instance().takeObjectAction("food")
        AIInterface.instance().setObjectDownAction("food")
#        AIInterface.instance().setObjectDownAction()
#        AIInterface.instance().setObjectDownAction()
#        AIInterface.instance().startIncantationAction()
        """

    @staticmethod
    def onLookAroundResult(tiles):
        print("onLookAroundResult")
        for tile in tiles:
            for item in tile:
                if item == "player":
                    continue
                AIInterface.instance().takeObjectAction(item)
#        AIInterface.instance().takeObjectAction(items[0][1])
        AIInterface.instance().inventoryAction()
        """
        nb = len(items[0]) - 1
        for i in range(0, nb):
            AIInterface.instance().takeObjectAction("food")
        """

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

    @staticmethod
    def onNbrOfTeamSlotsUnused(count):
        print(count)