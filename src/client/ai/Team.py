import os
from ai.Client import *

class Team:
    ressource_by_lvl_ = [{"player": 1, "linemate": 1, "deraumere": 0, "sibur": 0, "mendiane": 0, "phiras": 0, "thystame": 0},
                         {"player": 2, "linemate": 1, "deraumere": 1, "sibur": 1, "mendiane": 0, "phiras": 0, "thystame": 0},
                         {"player": 2, "linemate": 2, "deraumere": 0, "sibur": 1, "mendiane": 0, "phiras": 2, "thystame": 0},
                         {"player": 4, "linemate": 1, "deraumere": 1, "sibur": 2, "mendiane": 0, "phiras": 1, "thystame": 0},
                         {"player": 4, "linemate": 1, "deraumere": 2, "sibur": 1, "mendiane": 3, "phiras": 0, "thystame": 0},
                         {"player": 6, "linemate": 1, "deraumere": 2, "sibur": 3, "mendiane": 0, "phiras": 1, "thystame": 0},
                         {"player": 6, "linemate": 2, "deraumere": 2, "sibur": 2, "mendiane": 2, "phiras": 2, "thystame": 1}
                         ]

    def __init__(self):
        self.list_cli_ = list()
        self.list_cli_.append(Client(os.getpid()))
        self.attend_cli_ = 0
        self.max_lvl_ = 1

    # getter
    def getAttendClient(self):
        return self.attend_cli_

    def getMaxLvl(self):
        return self.max_Lvl_;

    def getListClient(self):
        return self.list_cli_

    #setter
    def setAttendClient(self, value):
        self.attend_cli_ = value

    def setMaxLvl(self, value):
        self.max_lvl_ = value


    #Methods
    def getClientByPid(self, value):
        return self.list_cli_.get(value)
