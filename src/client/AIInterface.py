
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
        return self.zappy.network.send_packet("Right")

    def turnLeftAction(self):
        return self.zappy.network.send_packet("Left")

    def moveForwardAction(self):
        return self.zappy.network.send_packet("Forward")

    def lookAroundAction(self):
        return self.zappy.network.send_packet("Look")

    def inventoryAction(self):
        return self.zappy.network.send_packet("Inventory")

    def broadcastAction(self, text):
        return self.zappy.network.send_packet("Broadcast {}".format(text))

    def numberOfTeamSlotsUnusedAction(self):
        return self.zappy.network.send_packet("Connect_nbr")

    def forkAction(self):
        return self.zappy.network.send_packet("Fork")

    def ejectPlayerTileAction(self):
        return self.zappy.network.send_packet("Eject")

    def takeObjectAction(self, object):
        return self.zappy.network.send_packet("Take {}".format(object))

    def setObjectDownAction(self, object):
        return self.zappy.network.send_packet("Set {}".format(object))

    def startIncantationAction(self):
        return self.zappy.network.send_packet("Incantation")