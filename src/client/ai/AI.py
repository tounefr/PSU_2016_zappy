from AIInterface import *
import time

class AI:
    def __init__(self):
        self.ai_interface = AIInterface()

    def BHV_FindFood(self):
        visible = self.ai_interface.lookAroundAction() # 7pts
        obj = "food"
        bSeeFood = 0
        for indexVisible in range(0, len(visible)):
            if (obj in visible[indexVisible]):
                bSeeFood = 1
                break;

        if (bSeeFood == 1):
            if (obj in visible[0]):
                self.ai_interface.takeObjectAction(obj)

    def onGameStart(self):
        print("Game start")
        self.ai_interface.forkAction()
        return
        while (1):
            inventory = self.ai_interface.inventoryAction() # 1pt
            if (inventory['food'] < 4):
                self.BHV_FindFood()

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
        print("onMessage: player_num={} message={}".format(player_num,  message))

    def onLevelUp(self, level):
        print("onLevelUp level={}".format(level))

    def onNbrOfTeamSlotsUnused(self, count):
        print(count)
