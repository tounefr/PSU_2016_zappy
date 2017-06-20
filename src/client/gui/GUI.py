
class GUI:
    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()

    def onGameStart(self):
        print("gui")

    def onMapSize(self):
        pass

    def onMapContent(self):
        pass

    def onTeamNames(self):
        pass

    def onPlayerConnect(self):
        pass

    def onPlayerPos(self):
        pass

    def onPlayerLevel(self):
        pass

    def onPlayerInventory(self):
        pass

    def onPlayerBroadcast(self):
        pass

    def onFirstPlayerTriggerSpell(self):
        pass

    def onEndSpell(self):
        pass

    def onPlayerLayEgg(self):
        pass

    def onPlayerThrowResource(self):
        pass

    def onPlayerTakeResource(self):
        pass

    def onPlayerDieOfHunger(self):
        pass

    def onPlayerLeddByAnotherPlayer(self):
        pass

    def onEggHatch(self):
        pass

    def onPlayerConnectedAfterHatch(self):
        pass

    def onEggDieOfHunger(self):
        pass

    def onServerTimeUnit(self):
        pass

    def onServerTimeUnitUpdated(self):
        pass

    def onEndGame(self):
        pass

    def onServerMessage(self):
        pass

    def onWrongCommand(self):
        pass

    def onWronCommandParameters(self):
        pass