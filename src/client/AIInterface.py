
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
        pass

    def getTeamName(self):
        pass

    def turnRight(self):
        packet = self.zappy.network.packet_router.getPacket("Right")
        self.zappy.network.send_packet(packet)

    def turnLeft(self):
        packet = self.zappy.network.packet_router.getPacket("Left")
        self.zappy.network.send_packet(packet)

    def moveForward(self):
        packet = self.zappy.network.packet_router.getPacket("Forward")
        self.zappy.network.send_packet(packet)

    def lookAroundAction(self):
        packet = self.zappy.network.packet_router.getPacket("Look")
        self.zappy.network.send_packet(packet)

    def inventoryAction(self):
        packet = self.zappy.network.packet_router.getPacket("Inventory")
        self.zappy.network.send_packet(packet)

    def broadcastAction(self):
        pass

    def getNumberOfTeamSlotsUnused(self):
        self.zappy.network.send_packet("Connect_nbr")

    def forkAction(self):
        self.zappy.network.send_packet("Fork")

    def ejectPlayerTileAction(self):
        self.zappy.network.send_packet("Eject")

    def takeObjectAction(self):
        self.zappy.network.send_packet("Take object")

    def setObjectDownAction(self):
        self.zappy.network.send_packet("Set object")

    def startIncantationAction(self):
        self.zappy.network.send_packet("Incantation")