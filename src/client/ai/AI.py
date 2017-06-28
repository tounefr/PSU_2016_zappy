from AIInterface import *
from Broadcast import *
from Team import *


class AI:

    def __init__(self):
        self.ai_interface = AIInterface()
        self.level = 1
        self.team_ = Team()
        self.broadcast_ = Broadcast(self.team_, self.ai_interface)


    def onGameStart(self):
        print("Game start")
        client = self.team_.list_cli_[0]
        while 1:
            inventory = self.ai_interface.inventoryAction()  # 1pt
            client.setInventory(inventory)
            self.broadcast_.brd_snd_inventory()
            if len(self.broadcast_.getMailBox()) > 0:
                print(self.broadcast_.getMailBox()[0])

            if inventory['food'] < 4:
                self.BHV_FindFood()
                """
            elif NbMessage() > 0:
                self.HandleMessages():
            else:
                self.FindStone()
                """

    def BHV_FindFood(self):
        direction = 0
        ko_count = 0
        client = self.team_.list_cli_[0]
        while 1:
            visible = self.ai_interface.lookAroundAction() # 7pts
            if self.TST_SeeObject(visible, "food") == 0:
                if ko_count == 0:
                    self.ai_interface.turnLeftAction() if direction == 0 else self.ai_interface.turnRightAction()
                else:
                    direction = (direction + 1) % 2
                    for x in range(0, self.level):
                        self.ai_interface.moveForwardAction()
                ko_count = (ko_count + 1) % 2
            else:
                self.ACT_MovToObject(visible, "food")
                while self.ai_interface.takeObjectAction("food") == "ok":
                    print("[AI] ~ Got some food")
                return 0


    def TST_SeeObject(self, visible, obj):
        for indexVisible in range(0, len(visible)):
            if obj in visible[indexVisible]:
                return 1
        return 0


    def ACT_MovToObject(self, visible, obj): # Ouai c'est dégueu... Mais c'est pas facile ca ^^'
        if obj in visible[0]:
            return 0
        index = self.ACT_GetClosestObject(visible, "food")
        print("[AI] (DEBUG) ~ food found at cell of index " + str(index))
        distance = self.ACT_GetDistanceToLine(index)
        for i in range(0, distance):
            self.ai_interface.moveForwardAction()
        print("[AI] (DEBUG) ~ distance " + str(distance))

        #  TEST ZONE
        nbCell = (2 ** (distance + 1) - ((distance + 1) % 2)) - (2 ** (distance) - (distance % 2))
        index = ((2 ** distance) - (distance % 2)) + 1
        middle = (int)((nbCell / 2) + (nbCell % 2))
        print("[AI] (DEBUG) << Nb of cells in the line: " + str(nbCell))
        print("[AI] (DEBUG) << On line index: " + str(index))
        print("[AI] (DEBUG) << Middle cell on line: " + str(middle))

        if index == middle:
            return 0

        self.ai_interface.turnLeftAction() if index < middle else self.ai_interface.turnRightAction()
        print("         [AI] (DEBUG) << Turn: " + "Left" if index < middle else "Right")
        distance = (index - middle) if index > middle else (middle - index)
        print("         [AI] (DEBUG) << Move: " + str(distance))
        for i in range(0, distance):
            self.ai_interface.moveForwardAction()
        return 0
        # !TEST ZONE


    def ACT_GetDistanceToLine(self, index):
        distance = 1
        for lvl in range(1, self.level + 1):
            if ((2 ** (lvl + 1)) - (lvl % 2)) >= index:
                return distance
            distance = distance + 1
        return 0


    def ACT_GetClosestObject(self, visible, obj):
        index = 0
        for cell in visible:
            if obj in cell:
                return index
            index = index + 1
        return 0


    def onPlayerEject(self, res):
        print("onPlayerEject res={}".format(res))


    def onPlayerDead(self, status):
        print("onPlayerDead")


    def onIncantation(self, status):
        if type(status) is int:
            print("Level up : {}".format(status))
        elif status == "underway":
            print("Underway")
        elif status == "ko":
            print("Incantation failed")


    def onMessage(self, player_num, message):
        message = self.broadcast_.stream_cipher(message, false)
        self.broadcast_.addMail(message)
        print("onMessage: player_num={} message={}".format(player_num,  message))


    def onLevelUp(self, level):
        print("onLevelUp level={}".format(level))


    def onNbrOfTeamSlotsUnused(self, count):
        print(count)
