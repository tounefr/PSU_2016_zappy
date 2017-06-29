import random
import string
from Client import *
from Team import *
from AIInterface import *

class Broadcast:
    def __init__(self, team, ai_interface, ai):
        self.team_ = team
        self.interface = ai_interface
        self.ai_ = ai
        self.broad_ = {
            " PID ": self.brd_rcv_pid,
            " WELCOME ": self.brd_rcv_welcome,
            " INVENTORY ": self.brd_rcv_inventory,
            " EAT_ON ": self.brd_rcv_eat_on,
            " EAT_OFF ": self.brd_rcv_eat_off,
            " GRP_RITUAL ": self.brd_rcv_grp_ritual,
            " AB_RITUAL ": self.brd_rcv_ab_ritual,
            " STR_RITUAL ": self.brd_rcv_str_ritual,
            " END_RITUAL ": self.brd_rcv_end_ritual,
            " FORK ": self.brd_rcv_fork
        }
        self.number_ = 0
        self.lastpid_ = ""
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
    def check_mail(self, key, funct, mail):
        res = False

        order = list(self.broad_.keys()).index(key)
        if order < 2:
            res = funct(mail[0], mail[1])
        else:
            try:
                split = mail[0].split(" ")[0]
                if int(split) != self.number_:
                    return res
                res = funct(mail[0], mail[1])
            except ...:
                return res
        return res

    def addMail(self, dist, text):
        text = self.stream_cipher(text, False)
        self.mailBox_.append((text, dist, self.number_))
        self.number_ += 1

    def readMail(self):
        rm = list()

        res = False
        incre = 0
        for mail in self.mailBox_:
            for key, value in self.broad_.items():
                if key in mail[0]:
                    if self.check_mail(key, value, mail):
                        res = True
            rm.append(incre)
            incre += 1
        for count in rm:
            del self.mailBox_[count]
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
        text = str(self.number_) + " PID "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        self.setNumber(self.getNumber() + 1)

    def brd_snd_welcome(self):
        if str(self.lastpid_) == "":
            return
        client = self.team_.list_cli_[0]
        text = "1" + " WELCOME "
        text += str(self.number_) + " "
        text += str(client.getPid()) + " " + str(self.lastpid_)

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        self.setNumber(self.getNumber() + 1)
        self.lastpid_ = 0

    def brd_snd_inventory(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " INVENTORY "
        text += str(client.getPid()) + " " + str(client.getLvl())
        for key, val in client.getInventory().items():
            text += ''.join(' {}={}'.format(key, val))

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        self.setNumber(self.getNumber() + 1)

    def brd_snd_eat_on(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " EAT_ON "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        self.setNumber(self.getNumber() + 1)


    def brd_snd_eat_off(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " EAT_OFF "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        self.setNumber(self.getNumber() + 1)

    def brd_snd_grp_ritual(self):

        self.setNumber(self.getNumber() + 1)
        return

    def brd_snd_ab_ritual(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " AB_RITUAL "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        self.setNumber(self.getNumber() + 1)

    def brd_snd_str_ritual(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " STR_RITUAL "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        self.setNumber(self.getNumber() + 1)

    def brd_snd_end_ritual(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " END_RITUAL "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        self.setNumber(self.getNumber() + 1)

    def brd_snd_fork(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " FORK "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)
        self.setNumber(self.getNumber() + 1)

    # rcv
    def brd_rcv_pid(self, text, dist):
        try:
            ign = text.split(" ", 2)[2]
            split = ign.split(" ")

            if len(split) != 1:
                return False
            self.lastpid_ = split[0]

            new_client = self.team_.getClientByPid(split[0])
            if new_client is not None:
                return False
            self.team_.getListClient().append(Client(int(self.lastpid_)))
        except ...:
            self.lastpid_ = ""
            return False
        return False

    def brd_rcv_welcome(self, text, dist):
        try:
            split = text.split(" ")
            if len(split) != 4:
                return False

            number = int(split[0])
            ign = text.split(" ", 2)[2]
            split = ign.split(" ")
            if self.team_.getListClient[0].getPid() != int(split[1]):
                return False

            self.setNumber(number)

            new_client = self.team_.getClientByPid(split[0])
            if new_client is not None:
                return False
            self.team_.getListClient().append(Client(int(split[0])))
        except ...:
            return False
        return False

    def brd_rcv_inventory(self, text, dist):
        try:
            ign = text.split(" ", 2)[2]
            split = ign.split(" ")

            client_rcv = self.team_.getClientByPid(int(split[0]))
            if client_rcv is None:
                return False

            client_rcv.setLvl(int(split[1]))

            inv = {}
            ign = ign.split(" ", 4)[4]
            split = ign.split(" ")

            for chain in split:
                chain_split = chain.split("=")
                inv[chain_split[0]] = int(chain_split[1])

            client_rcv.setInventory(inv)
        except ...:
            return False
        return False

    def brd_rcv_eat_on(self, text, dist):
        try:
            ign = text.split(" ", 2)[2]
            split = ign.split(" ")

            client_rcv = self.team_.getClientByPid(int(split[0]))
            if client_rcv is None:
                return False
            client_rcv.setIsEating(True)
        except ...:
            return False
        return False

    def brd_rcv_eat_off(self, text, dist):
        try:
            ign = text.split(" ", 2)[2]
            split = ign.split(" ")

            client_rcv = self.team_.getClientByPid(int(split[0]))
            if client_rcv is None:
                return False
            client_rcv.setIsEating(False)
        except ...:
            return False
        return False

    def brd_rcv_grp_ritual(self, text, dist):
        return True

    def brd_rcv_ab_ritual(self, text, dist):
        try:
            ign = text.split(" ", 2)[2]
            split = ign.split(" ")

            client_rcv = self.team_.getClientByPid(int(split[0]))
            if client_rcv is None:
                return True
            client_rcv.setIsRitual(False)
        except ...:
            return True
        return True

    def brd_rcv_str_ritual(self, text, dist):
        try:
            ign = text.split(" ", 2)[2]
            split = ign.split(" ")

            client_rcv = self.team_.getClientByPid(int(split[0]))
            if client_rcv is None:
                return True
            client_rcv.setIsRitual(True)
        except ...:
            return True
        return True

    def brd_rcv_end_ritual(self, text, dist):
        try:
            ign = text.split(" ", 2)[2]
            split = ign.split(" ")

            client_rcv = self.team_.getClientByPid(int(split[0]))
            if client_rcv is None:
                return True
            client_rcv.setIsRitual(True)
        except ...:
            return True
        return True

    def brd_rcv_fork(self, text, dist):
        self.team_.setAttendList(self.team_.getAttendList() + 1)
        return False
