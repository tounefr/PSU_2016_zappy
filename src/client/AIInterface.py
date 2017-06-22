
class AIInterface:

    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()

    def isRunning(self):
        return self.zappy.running

    def getMapSize(self):
        return self.zappy.map_size

    def getTeamName(self):
        return self.zappy.team_name

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