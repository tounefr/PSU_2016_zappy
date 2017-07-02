import decimal
from decimal import Decimal
from core.AIInterface import *
from ai.Broadcast import *
from ai.Team import *

class AI:
    def __init__(self):
        self.ai_interface = AIInterface()
        self.team_ = Team()
        self.broadcast_ = Broadcast(self.team_, self.ai_interface, self)

    def onGameStart(self):
        print("Game start")
        client = self.team_.list_cli_[0]
        self.broadcast_.brd_snd_pid()

        while 1:
            inventory = self.ai_interface.inventoryAction()  # 1pt
            client.setInventory(inventory)

            if inventory['food'] < 6:
                self.BHV_FindFood()
                continue
            else:
                if self.broadcast_.readMail():
                    continue
                else:
                    self.TST_TooMuchClient(client)
                    self.broadcast_.brd_snd_inventory()  # 7pts
                    if self.TST_RitualCondi(client):
                        continue
                    else:
                        self.BHV_FindStone()

    def BHV_FindStone(self):
        direction = 0
        ko_count = 0

        count_turn = 0
        client = self.team_.list_cli_[0]
        while 1:
            if self.broadcast_.readMail():
                return
            visible = self.ai_interface.lookAroundAction()
            incre = -1
            if self.TST_SeeObject(visible, "thystame") == 1:
                nbr = self.ACT_MovToObject(visible, "thystame", client)
                while ++incre < nbr and self.ai_interface.takeObjectAction("thystame") == "ok":
                    client.getInventory()['thystame'] += 1
                return 0
            elif self.TST_SeeObject(visible, "phiras") == 1:
                nbr = self.ACT_MovToObject(visible, "phiras", client)
                while ++incre < nbr and self.ai_interface.takeObjectAction("phiras") == "ok":
                    client.getInventory()['phiras'] += 1
                return 0
            elif self.TST_SeeObject(visible, "mendiane") == 1:
                nbr = self.ACT_MovToObject(visible, "mendiane", client)
                while ++incre < nbr and self.ai_interface.takeObjectAction("mendiane") == "ok":
                    client.getInventory()['mendiane'] += 1
                return 0
            elif self.TST_SeeObject(visible, "sibur") == 1:
                nbr = self.ACT_MovToObject(visible, "sibur", client)
                while ++incre < nbr and self.ai_interface.takeObjectAction("sibur") == "ok":
                    client.getInventory()['sibur'] += 1
                return 0
            elif self.TST_SeeObject(visible, "deraumere") == 1:
                nbr = self.ACT_MovToObject(visible, "deraumere", client)
                while ++incre < nbr and self.ai_interface.takeObjectAction("deraumere") == "ok":
                    client.getInventory()['deraumere'] += 1
                return 0
            elif self.TST_SeeObject(visible, "linemate") == 1:
                nbr = self.ACT_MovToObject(visible, "linemate", client)
                while ++incre < nbr and self.ai_interface.takeObjectAction("linemate") == "ok":
                    client.getInventory()['linemate'] += 1
                return 0
            else:
                if ko_count == 0:
                    self.ai_interface.turnLeftAction() if direction == 0 else self.ai_interface.turnRightAction()
                else:
                    direction = (direction + 1) % 2
                    for x in range(0, client.getLvl()):
                        self.ai_interface.moveForwardAction()
                ko_count = (ko_count + 1) % 2

    def BHV_FindFood(self):
        self.broadcast_.brd_snd_eat_on()
        direction = 0
        ko_count = 0
        #
        count_turn = 0
        client = self.team_.getListClient()[0]
        while client.getInventory()['food'] < 16:
            self.broadcast_.readMail(False)
            visible = self.ai_interface.lookAroundAction()  # 7pts
            if self.TST_SeeObject(visible, "food") == 0:
                if ko_count == 0:
                    self.ai_interface.turnLeftAction() if direction == 0 else self.ai_interface.turnRightAction()
                    ko_count = 1
                    count_turn += 1

                elif ko_count == 1:
                    ko_count = 0
                    direction = (direction + 1) % 2
                    for x in range(0, client.getLvl()):
                        self.ai_interface.moveForwardAction()
            else:
                ko_count = 0
                nbr = self.ACT_MovToObject(visible, "food", client)
                if nbr != -1:
                    incre = -1
                    while ++incre < nbr and self.ai_interface.takeObjectAction("food") == "ok":
                        client.getInventory()['food'] += 1

            if count_turn == 3:
                self.ai_interface.turnLeftAction() if direction == 0 else self.ai_interface.turnRightAction()
                count_turn = 0

        self.broadcast_.brd_snd_eat_off()

    def BHV_fork(self):
        self.broadcast_.brd_snd_fork()
        self.ai_interface.forkAction()

    def BHV_SetRoleRitual(self, client, material):
        try:
            material[client.getPid()][""]
        except ValueError:
            return 0

    def TST_RitualCondi(self, client):
        res = False

        if client.getLvl() == 1:
            if self.TST_TooManyRessources(self.team_.getRessouceByLvl()[client.getLvl() - 1],
                                          client.getInventory()):
                res = True
                self.broadcast_.brd_snd_str_ritual()
                self.ai_interface.setObjectDownAction("linemate")
                client.getInventory()["linemate"] -= 1
                if self.ai_interface.startIncantationAction() != "ko":
                    client.setLvl(client.getLvl() + 1)
                self.broadcast_.brd_snd_end_ritual()
        else:
            lvl_requirement = dict(self.team_.getRessouceByLvl()[client.getLvl() - 1])
            same_lvl, other = [], []
            list_client = self.team_.getListClient()

            print("****************")
            same_lvl.append(client)
            for x in list_client:
                if x.getPid() == client.getPid():
                    continue
                (same_lvl, other)[x.getLvl() != client.getLvl()].append(x)

            if len(same_lvl) < lvl_requirement['player']:
                return False

            material = {}
            other.sort()
            ord_list = same_lvl + other

            eject_count = 4
            for cli in ord_list:
                lis = {cli.getPid(): {}}
                if lvl_requirement['player'] > 0 and cli.getLvl() == client.getLvl():
                    lis[cli.getPid()]['lvl'] = 1
                    lvl_requirement['player'] -= 1
                else:
                    lis[cli.getPid()]['lvl'] = 0

                if lis[cli.getPid()]['lvl'] != 1 and eject_count > 0:
                    lis[cli.getPid()]['eject'] = 1
                    eject_count -= 1
                else:
                    lis[cli.getPid()]['eject'] = 0
                cpy_inven = dict(cli.getInventory())
                lis[cli.getPid()]['inventory'] = {}
                for key, value in cpy_inven.items():
                    if key != "food":
                        if lvl_requirement[key] > 0 and cpy_inven[key] > 0:
                            lis[cli.getPid()]['inventory'][key] = 0
                            while lvl_requirement[key] > 0 and cpy_inven[key] > 0:
                                lvl_requirement[key] -= 1
                                cpy_inven[key] -= 1
                                lis[cli.getPid()]['inventory'][key] += 1

                if len(lis[cli.getPid()]['inventory']) == 0:
                    lis[cli.getPid()]['conso'] = 0
                else:
                    lis[cli.getPid()]['conso'] = 1

                if lis[cli.getPid()]['conso'] == 1 or lis[cli.getPid()]['lvl'] == 1 or lis[cli.getPid()]['eject'] == 1:
                    material.append(lis)

            print("[debug] - requirements = {}".format(lvl_requirement))
            print("[DEBUG] - ok - {}".format(material))
            for key, value in lvl_requirement.items():
                if value > 0:
                    return False

            #doit faire la pose de pierre du client actuel
            #ensuite lancer le material en broadcast
            #puis faire la reception
        return res

    def TST_TooManyRessources(self, lvl_ress, inventory):
        res = True

        for key in inventory:
            if key not in "food":
                if lvl_ress[key] > inventory[key]:
                    res = False
        return res

    def TST_TooMuchClient(self, client):
        count = self.ai_interface.numberOfTeamSlotsUnusedAction()
        count += self.team_.getAttendClient()

        needed = self.team_.getRessouceByLvl()[(self.team_.getMaxLvl() - 1)].get('player')
        if needed is None:
            return
        while count < needed and client.getInventory()["food"] > 4:
            self.BHV_fork()
            count += 1
        return

    def TST_SeeObject(self, visible, obj):
        for indexVisible in range(0, len(visible)):
            if obj in visible[indexVisible]:
                return 1
        return 0

    def ACT_MovToObject(self, visible, obj, client):
        if obj in visible[0]:
            return 0
        index = self.ACT_GetClosestObject(visible, obj)
        if index == -1:
            return -1
        number = 0
        for cell in visible[index]:
            if cell in obj:
                number += 1
        distance = self.ACT_GetDistanceToLine(index, client)
        for i in range(0, distance):
            self.ai_interface.moveForwardAction()

        middle_act_line = (2 ** (distance + 1)) - (distance % 2) - (distance)
        if index == middle_act_line:
            return number
        elif index < middle_act_line:
            self.ai_interface.turnLeftAction()
            distance = middle_act_line - index
        else:
            self.ai_interface.turnRightAction()
            distance = index - middle_act_line

        for i in range(0, distance):
            self.ai_interface.moveForwardAction()
        return number

    def ACT_GetDistanceToLine(self, index, client):
        distance = 0
        for lvl in range(1, client.getLvl() + 1):
            distance += 1
            if ((2 ** (lvl + 1)) - (lvl % 2)) > index:
                return distance
        return distance

    def ACT_GetClosestObject(self, visible, obj):
        index = 0
        for cell in visible:
            if obj in cell:
                return index
            index += 1
        return -1

    def onPlayerEject(self, res):
        print("onPlayerEject res={}".format(res))

    def onPlayerDead(self, status):
        print("onPlayerDead")

    def onMessage(self, player_num, message):
        self.broadcast_.addMail(str(player_num), message)
        print("onMessage: player_num={} message={}".format(player_num, message))

    def onNbrOfTeamSlotsUnused(self, count):
        print(count)
