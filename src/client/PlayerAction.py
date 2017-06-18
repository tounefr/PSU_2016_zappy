from enum import Enum
from ZappyClient import *

class MovementEnum(Enum):
    FORWARD = 0,
    RIGHT = 1,
    LEFT = 2

class PlayerAction:

    def __init__(self):
        self.zappy = ZappyClient.instance()

    def moveAction(self, movementAction):
        if movementAction == MovementEnum.FORWARD:
            self.zappy.network.send_packet("Forward")
        elif movementAction == MovementEnum.RIGHT:
            self.zappy.network.send_packet("Right")
        elif movementAction == MovementEnum.LEFT:
            self.zappy.network.send_packet("Left")

    def lookAroundAction(self):
        self.zappy.network.send_packet("Look")

    def inventoryAction(self):
        self.zappy.network.send_packet("Inventory")

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