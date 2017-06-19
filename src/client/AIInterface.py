
class AIInterface:

    g_instance = None

    @staticmethod
    def instance():
        if AIInterface.g_instance is None:
            AIInterface.g_instance = AIInterface()
        return AIInterface.g_instance

    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()

    def getMapSize(self):
        return 0

    def getTeamName(self):
        return 0

    def turnRightAction(self):
        self.zappy.network.send("Right")

    def turnLeftAction(self):
        self.zappy.network.send("Left")

    def moveForwardAction(self):
        self.zappy.network.send("Forward")

    def lookAroundAction(self):
        self.zappy.network.send("Look")

    def inventoryAction(self):
        self.zappy.network.send("Inventory")

    def broadcastAction(self, text):
        self.zappy.network.send("Broadcast {}".format(text))

    def numberOfTeamSlotsUnusedAction(self):
        self.zappy.network.send("Connect_nbr")

    def forkAction(self):
        self.zappy.network.send("Fork")

    def ejectPlayerTileAction(self):
        self.zappy.network.send("Eject")

    def takeObjectAction(self):
        self.zappy.network.send("Take object")

    def setObjectDownAction(self):
        self.zappy.network.send("Set object")

    def startIncantationAction(self):
        self.zappy.network.send("Incantation")