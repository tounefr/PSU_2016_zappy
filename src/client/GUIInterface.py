
class GUIInterface:

    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()

    def getMapSize(self):
        pass

    def getTileContent(self):
        pass

    def getMapContent(self):
        pass

    def getPlayerPosition(self):
        pass

    def getPlayerLevel(self):
        pass

    def getPlayerInventory(self):
        pass

    def askCurrentUnitTimeServer(self):
        pass

    def updateUnitTimeServer(self):
        pass