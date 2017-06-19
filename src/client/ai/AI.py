from AIInterface import *

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
        AIInterface.instance().moveAction("forward")
        AIInterface.instance().moveAction("left")

    @staticmethod
    def onMovement(direction, res):
        print("onMovement dir={} res={}".format(direction, res))
        AIInterface.instance().lookAroundAction()

    @staticmethod
    def onLookAroundResult(items):
        print("onLookAroundResult")
        print(items)

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

