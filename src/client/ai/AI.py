from AIInterface import *
import time

class AI:
    def __init__(self):
        self.ai_interface = AIInterface()

    def onGameStart(self):
        print("Game start")

        while self.ai_interface.isRunning():
            self.ai_interface.moveForwardAction()
            self.ai_interface.broadcastAction("forward")
            time.sleep(1)

        """
        while (1):
            visible = self.ai_interface.lookAroundAction() #7pts
            print("On my cell, I can see:")
            for obj in visible[0]:
                print(" > " + obj)
            print(" END")

            for obj in visible[0]:
                self.ai_interface.takeObjectAction(obj) #7pts
            self.ai_interface.moveForwardAction() #7pts
        """


        '''
        print("Turn right result : {}".format(self.ai_interface.turnRightAction()))
        print("Turn left result : {}".format(self.ai_interface.turnLeftAction()))
        print("Move forward result : {}".format(self.ai_interface.moveForwardAction()))
        print("Look Around result : {}".format(self.ai_interface.lookAroundAction()))
        print("Inventory result : {}".format(self.ai_interface.inventoryAction()))
        print("Broadcast result : {}".format(self.ai_interface.broadcastAction("salut tout le monde")))
        print("numberOfTeamSlotsUnusedAction result : {}".format(self.ai_interface.numberOfTeamSlotsUnusedAction()))
        print("fork result : {}".format(self.ai_interface.forkAction()))
#       bugged
#        print("ejectPlayerTileAction result : {}".format(self.ai_interface.ejectPlayerTileAction()))
        print("takeObjectAction result : {}".format(self.ai_interface.takeObjectAction("food")))
        print("setObjectDownAction result : {}".format(self.ai_interface.setObjectDownAction("food")))
#       bugged
#        print("startIncantationAction result : {}".format(self.ai_interface.startIncantationAction()))
        '''

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
