from PlayerAction import *

class AI:

    @staticmethod
    def on_start():
        print("Game start")
        PlayerAction.instance().lookAroundAction()

    @staticmethod
    def onMovement(direction, res):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

        print("onMovement dir={} res={}".format(direction, res))
        PlayerAction.instance().lookAroundAction()

    @staticmethod
    def onLookAroundResult(items):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

        print("onLookAroundResult")
        print(items)
        PlayerAction.instance().inventoryAction()

    @staticmethod
    def onInventoryContent(inventory):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

        print("onInventoryContent")
        print(inventory)

    @staticmethod
    def onPlayerForked():
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

    @staticmethod
    def onPlayerEject(res):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

        print("onPlayerEject res={}".format(res))

    @staticmethod
    def onPlayerDead():
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

        print("onPlayerDead")

    @staticmethod
    def onTakeObject(res):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

        print("onTakeObject res={}".format(res))

    @staticmethod
    def onObjectDown(res):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance

        print("onObjectDown res={}".format(res))

    @staticmethod
    def onIncantationFinished():
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

