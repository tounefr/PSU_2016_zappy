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
            "PID": self.brd_rcv_pid,
            "WELCOME": self.brd_rcv_welcome,
            "INVENTORY": self.brd_rcv_inventory,
            "EAT_ON": self.brd_rcv_eat_on,
            "EAT_OFF": self.brd_rcv_eat_off,
            "GRP_RITUAL": self.brd_rcv_grp_ritual,
            "AB_RITUAL": self.brd_rcv_ab_ritual,
            "STR_RITUAL": self.brd_rcv_str_ritual,
            "END_RITUAL": self.brd_rcv_end_ritual,
            "FORK": self.brd_rcv_fork
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
    def check_mail(self, key, funct, mail, content):
        res = False

        order = list(self.broad_.keys()).index(key)
        if order < 2:
            res = funct(mail[0], mail[1])
        else:
            try:
                split = content['number']
                print(" ------------ ")
                print("[DEBUG] [check_mail] - message [{}]".format(mail[0]))
                print("[DEBUG] [check_mail] - number -> ({} - {})".format(split, self.number_))
                print(" ------------ ")
                if int(split) != self.number_:
                    return res
                res = funct(content, mail[1])
            except TypeError:
                return res
            except ValueError:
                return res
        return res

    def addMail(self, dist, text):
        text = self.stream_cipher(text, False)
        self.mailBox_.append((text, dist, self.number_))
        self.setNumber(self.getNumber() + 1)

    def readMail(self):
        rm = list()

        res = False
        incre = 0
        for mail in self.mailBox_:
            content = json.loads(mail[0])
            for key, value in self.broad_.items():
                if key in content['cmd']:
                    if self.check_mail(key, value, mail, content):
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

    def brd_snd_welcome(self):
        if str(self.lastpid_) == "":
            return
        client = self.team_.list_cli_[0]
        content = {
            "number": self.number_,
            "cmd": "PID",
            "pid": client.getPid(),
            "new_player_pid" : str(self.lastpid_)
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        self.interface.broadcastAction(text)
        self.lastpid_ = 0

    def brd_snd_inventory(self):
        client = self.team_.list_cli_[0]

        content = {
            "number": self.number_,
            "cmd": "PID",
            "pid": client.getPid(),
            "lvl": client.getLvl(),
            "inventory": client.getInventory()
        }

        self.setNumber(self.getNumber() + 1)

        text = json.dumps(content)
        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)

    def brd_snd_eat_on(self):
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

    def brd_snd_eat_off(self):
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

    def brd_snd_grp_ritual(self):

        self.setNumber(self.getNumber() + 1)
        return

    def brd_snd_ab_ritual(self):
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

    def brd_snd_str_ritual(self):
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

    def brd_snd_end_ritual(self):
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

    def brd_snd_fork(self):
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

    # rcv
    def brd_rcv_pid(self, json, dist):
        try:
            self.lastpid_ = json['pid']

            new_client = self.team_.getClientByPid(self.lastpid_)
            if new_client is not None:
                return False
            self.team_.getListClient().append(Client(int(self.lastpid_)))
            self.brd_snd_welcome()
        except TypeError:
            self.lastpid_ = 0
            return False
        except ValueError:
            self.lastpid_ = 0
            return False
        return False

    def brd_rcv_welcome(self, json, dist):
        try:
            self.setNumber(json['number'])

            new_client = self.team_.getClientByPid(json['new_player_pid'])
            if new_client is not None:
                return False
            self.team_.getListClient().append(Client(json['new_player_pid']))
            self.setNumber(json['number'] + 1)
        except TypeError:
            return False
        except ValueError:
            return False
        return False

    def brd_rcv_inventory(self, json, dist):
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
        return False

    def brd_rcv_eat_on(self, json, dist):
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return False
            client_rcv.setIsEating(True)
        except TypeError:
            return False
        except ValueError:
            return False
        return False

    def brd_rcv_eat_off(self, json, dist):
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return False
            client_rcv.setIsEating(False)
        except TypeError:
            return False
        except ValueError:
            return False
        return False

    def brd_rcv_grp_ritual(self, json, dist):
        try:
            if dist != 0:
                return True
        except TypeError:
            return True
        except ValueError:
            return True
        return True

    def brd_rcv_ab_ritual(self, json, dist):
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return True
            client_rcv.setIsRitual(False)
        except ValueError:
            return True
        return True

    def brd_rcv_str_ritual(self, json, dist):
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return True
            client_rcv.setIsRitual(True)
        except ValueError:
            return False
        return True

    def brd_rcv_end_ritual(self, json, dist):
        try:
            client_rcv = self.team_.getClientByPid(json['pid'])
            if client_rcv is None:
                return True
            client_rcv.setIsRitual(False)
        except ValueError:
            return False
        return True

    def brd_rcv_fork(self, json, dist):
        self.team_.setAttendList(self.team_.getAttendList() + 1)
        return False
