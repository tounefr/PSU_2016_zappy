
class Client:

    def __init__(self, pid):
        self.pid_ = pid;
        self.lvl_ = 1
        self.is_eating_ = 0
        self.is_ritual_ = 0
        self.inventory_ = {"food": 10, "linemate": 0, "deraumere": 0, "sibur": 0, "mendiane": 0, "phiras": 0, "thystame": 0}


    #getter
    def getPid(self):
        return self.pid_

    def getInventory(self):
        return self.inventory_

    def getLvl(self):
        return self.lvl_

    def isEating(self):
        return self.is_eating_

    def isRitual(self):
        return self.is_ritual_



    #setter
    def setInventory(self, inv):
        self.inventory_ = inv

    def setLvl(self, value):
        self.lvl_ = value

    def setIsEating(self, value):
        self.is_eating_ = value

    def setIsRitual(self, value):
        self.is_ritual_ = value

    def canGrp(self):
        if self.is_ritual_ == 1 or self.is_eating_ == 1:
            return 0
        return 1

    #sort
    def __lt__(self, other):
        return self.getLvl() < other.getLvl()
