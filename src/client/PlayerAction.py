
class PlayerAction:
    g_instance = None

    @staticmethod
    def instance():
        if PlayerAction.g_instance is None:
            PlayerAction.g_instance = PlayerAction()
        return PlayerAction.g_instance

    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()

    def moveAction(self, movement):
        if movement not in ["forward", "left", "right"]:
            raise RuntimeError("Unknown movement")
        movement = movement[0].upper()
        packet = self.zappy.network.packet_router.getPacket(movement)
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