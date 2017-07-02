import random
import string
import json
from ai.Client import *
from ai.Team import *
from core.AIInterface import *

class Broadcast:
    def __init__(self, team, ai_interface, ai):
        self.team_ = team
        self.interface = ai_interface
        self.ai_ = ai
        self.broad_ = {
            "PID": [self.brd_rcv_pid, False],
            "WELCOME": [self.brd_rcv_welcome, False],
            "INVENTORY": [self.brd_rcv_inventory, False],
            "EAT_ON": [self.brd_rcv_eat_on, False],
            "EAT_OFF": [self.brd_rcv_eat_off, False],
            "GRP_RITUAL": [self.brd_rcv_grp_ritual, True],
            "AB_RITUAL": [self.brd_rcv_ab_ritual, True],
            "STR_RITUAL": [self.brd_rcv_str_ritual, True],
            "END_RITUAL": [self.brd_rcv_end_ritual, True],
            "FORK": [self.brd_rcv_fork, False]
        }
        self.number_ = 0
        self.lastpid_ = 0
        self.key_ = 0
        self.mailBox_ = list()
        for char in self.interface.getTeamName():
            self.key_ += ord(char)

    # getter
    def getNumber(self):
        return self.number_

    def getMailBox(self):
        return self.mailBox_

    # setter
    def setNumber(self, value):
        self.number_ = value

    # Methods
    def funct_in_dict_doesnt_work(self, key, mail):
        res = False
        if key in "PID":
            res = self.brd_rcv_pid(mail[0], mail[1])
        elif key in "WELCOME":
            res = self.brd_rcv_welcome(mail[0], mail[1])
        elif key in "INVENTORY":
            res = self.brd_rcv_inventory(mail[0], mail[1])
        elif key in "EAT_ON":
            res = self.brd_rcv_eat_on(mail[0], mail[1])
        elif key in "EAT_OFF":
            res = self.brd_rcv_eat_off(mail[0], mail[1])
        elif key in "GRP_RITUAL":
            res = self.brd_rcv_grp_ritual(mail[0], mail[1])
        elif key in "AB_RITUAL":
            res = self.brd_rcv_ab_ritual(mail[0], mail[1])
        elif key in "STR_RITUAL":
            res = self.brd_rcv_str_ritual(mail[0], mail[1])
        elif key in "END_RITUAL":
            res = self.brd_rcv_end_ritual(mail[0], mail[1])
        elif key in "FORK":
            res = self.brd_rcv_fork(mail[0], mail[1])
        return res

    def check_mail(self, key, mail):
        res = False

        print(" ------------ ")
        if key in "PID" or key in "WELCOME":
            split = mail[0]['number']
            print("[DEBUG] [check_mail _ 1] - {} - message [{}]".format(key, mail[0]))
            res = self.funct_in_dict_doesnt_work(key, mail)
            print("[DEBUG] [check_mail _ 1] - number -> ({} - {})".format(split, mail[2]))
            print(" ------------ ")
        else:
            split = mail[0]['number']
            print("[DEBUG] [check_mail] - {} - message [{}]".format(key, mail[0]))
            print("[DEBUG] [check_mail] - number -> ({} - {})".format(split, mail[2]))
            print(" ------------ ")
            #if split != mail[2]:
            #    return res
            res = self.funct_in_dict_doesnt_work(key, mail)
        return res

    def addMail(self, dist, text):
        text = self.stream_cipher(text, False)
        try:
            content = json.loads(text)
        except ValueError:
            return
        self.mailBox_.append((content, dist, self.number_))
        self.setNumber(self.getNumber() + 1)

    def readMail(self, act=True):
        rm = list()

        res = False
        incre = 0
        for mail in self.mailBox_:
            print("[DEBUG] [readMail] - av content = {}".format(mail[0]))
            for key, value in self.broad_.items():
                if key in mail[0]['cmd']:
                    if act is True or value[1] is False:
                        if self.check_mail(key, mail):
                            res = True
                        rm.append(incre)
            incre += 1
        incre = 0
        for count in rm:
            print("[DEBUG] [readMail] - delete {}".format(count - incre))
            del self.mailBox_[count - incre]
            incre += 1
        return res

    def shift(self, current_position, distance, direction: (0, 1)):
        direction = 1 if direction else -1
        return current_position + direction * distance

    def stream_cipher(self, message, do_encrypt=True):
        random.seed(self.key_)
        characters = 2 * (
            string.ascii_letters +
            string.digits +
            string.punctuation + ' '
        )
        lenchars = len(characters) // 2
        return ''.join([characters[
                            self.shift(characters.index(message[each_char]), lenchars - int(lenchars * random.random()),
                                  do_encrypt)] for each_char in range(len(message))])

    # snd
    def brd_snd_pid(self):
        print("[DEBUG] [brd_send_pid] - rentre")
        client = self.team_.list_cli_[0]
        content = {
            "number": self.number_,
            "cmd": "PID",
            "pid": client.getPid()
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        print("[DEBUG] [brd_send_pid] - sort")

    def brd_snd_welcome(self):
        print("[DEBUG] [brd_snd_welcome] - rentre")
        if str(self.lastpid_) == 0:
            return
        client = self.team_.list_cli_[0]
        content = {
            "number": self.number_,
            "cmd": "WELCOME",
            "pid": client.getPid(),
            "new_player_pid" : self.lastpid_,
            "attend": self.team_.getAttendClient()
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        self.lastpid_ = 0
        print("[DEBUG] [brd_send_welcome] - sort")

    def brd_snd_inventory(self):
        print("[DEBUG] [brd_snd_inventory] - rentre")
        client = self.team_.list_cli_[0]

        content = {
            "number": self.number_,
            "cmd": "INVENTORY",
            "pid": client.getPid(),
            "lvl": client.getLvl(),
            "inventory": client.getInventory()
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        print("[DEBUG] [brd_send_inventory] - sort")

    def brd_snd_eat_on(self):
        print("[DEBUG] [brd_snd_eat_on] - rentre")
        client = self.team_.list_cli_[0]
        content = {
            "number": self.number_,
            "cmd": "EAT_ON",
            "pid": client.getPid()
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        print("[DEBUG] [brd_send_eat_on] - sort")

    def brd_snd_eat_off(self):
        print("[DEBUG] [brd_snd_eat_off] - rentre")
        client = self.team_.list_cli_[0]
        content = {
            "number": self.number_,
            "cmd": "EAT_OFF",
            "pid": client.getPid()
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        print("[DEBUG] [brd_send_eat_off] - sort")

    def brd_snd_grp_ritual(self):
        print("[DEBUG] [brd_snd_grp_ritual] - rentre")

        self.setNumber(self.getNumber() + 1)
        print("[DEBUG] [brd_send_grp_ritual] - sort")
        return

    def brd_snd_ab_ritual(self):
        print("[DEBUG] [brd_snd_ab_ritual] - rentre")
        client = self.team_.list_cli_[0]
        content = {
            "number": self.number_,
            "cmd": "AB_RITUAL",
            "pid": client.getPid()
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        print("[DEBUG] [brd_send_ab_ritual] - sort")

    def brd_snd_str_ritual(self):
        print("[DEBUG] [brd_snd_str_ritual] - rentre")
        client = self.team_.list_cli_[0]
        content = {
            "number": self.number_,
            "cmd": "STR_RITUAL",
            "pid": client.getPid()
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        print("[DEBUG] [brd_send_str_ritual] - sort")

    def brd_snd_end_ritual(self):
        print("[DEBUG] [brd_snd_end_ritual] - rentre")
        client = self.team_.list_cli_[0]
        content = {
            "number": self.number_,
            "cmd": "END_RITUAL",
            "pid": client.getPid()
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        print("[DEBUG] [brd_send_end_ritual] - sort")

    def brd_snd_fork(self):
        print("[DEBUG] [brd_snd_fork] - rentre")
        client = self.team_.list_cli_[0]
        content = {
            "number": self.number_,
            "cmd": "FORK",
            "pid": client.getPid()
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        print("[DEBUG] [brd_send_fork] - sort")

    # rcv
    def brd_rcv_pid(self, json, dist):
        print("[debug] [brd_rcv_pid] - rentre")
        try:
            self.lastpid_ = json['pid']
            new_client = self.team_.getClientByPid(self.lastpid_)
            if new_client is not None:
                return False
            self.team_.getListClient().append(Client(self.lastpid_))
            self.brd_snd_welcome()
        except TypeError:
            self.lastpid_ = 0
            return False
        except ValueError:
            self.lastpid_ = 0
            return False
        print("[DEBUG] [brd_rcv_pid] - sort")
        return False

    def brd_rcv_welcome(self, json, dist):
        print("[debug] [brd_rcv_welcome] - rentre")
        try:

            new_client = self.team_.getClientByPid(json['pid'])
            if new_client is not None:
                return False
            self.setNumber(json['number'] + 1)
            self.team_.setAttendClient(json['attend'])
            self.team_.getListClient().append(Client(json['pid']))
        except TypeError:
            return False
        except ValueError:
            return False
        print("[DEBUG] [brd_rcv_welcome] - sort")
        return False

    def brd_rcv_inventory(self, json, dist):
        print("[debug] [brd_rcv_inventory] - rentre")
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return False

            client_rcv.setLvl(json['lvl'])
            client_rcv.setInventory(json['inventory'])
        except TypeError:
            return False
        except ValueError:
            return False
        print("[DEBUG] [brd_rcv_inventory] - sort")
        return False

    def brd_rcv_eat_on(self, json, dist):
        print("[debug] [brd_rcv_eat_on] - rentre")
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return False
            client_rcv.setIsEating(True)
        except TypeError:
            return False
        except ValueError:
            return False
        print("[DEBUG] [brd_rcv_eat_on] - sort")
        return False

    def brd_rcv_eat_off(self, json, dist):
        print("[debug] [brd_rcv_eat_off] - rentre")
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return False
            client_rcv.setIsEating(False)
        except TypeError:
            return False
        except ValueError:
            return False
        print("[DEBUG] [brd_rcv_eat_off] - sort")
        return False

    def brd_rcv_grp_ritual(self, json, dist):
        print("[debug] [brd_rcv_grp_ritual] - rentre")
        try:
            if dist != 0:
                return True
        except TypeError:
            return True
        except ValueError:
            return True
        print("[DEBUG] [brd_rcv_grp_ritual] - sort")
        return True

    def brd_rcv_ab_ritual(self, json, dist):
        print("[debug] [brd_rcv_ab_ritual] - rentre")
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return True
            client_rcv.setIsRitual(False)
        except ValueError:
            return True
        print("[DEBUG] [brd_rcv_ab_ritual] - sort")
        return True

    def brd_rcv_str_ritual(self, json, dist):
        print("[debug] [brd_rcv_str_ritual] - rentre")
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return True
            client_rcv.setIsRitual(True)
        except ValueError:
            return False
        print("[DEBUG] [brd_rcv_str_ritual] - sort")
        return True

    def brd_rcv_end_ritual(self, json, dist):
        print("[debug] [brd_rcv_end_ritual] - rentre")
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return True
            client_rcv.setIsRitual(False)
        except ValueError:
            return False
        print("[DEBUG] [brd_end_ritual] - sort")
        return True

    def brd_rcv_fork(self, json, dist):
        print("[debug] [brd_rcv_fork] - rentre")
        self.team_.setAttendList(self.team_.getAttendClient() + 1)
        print("[DEBUG] [brd_rcv_fork] - sort")
        return False
