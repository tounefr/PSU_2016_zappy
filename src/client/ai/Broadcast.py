import random
import string
from ai.Client import *
from ai.Team import *
from core.AIInterface import *

class Broadcast:
    def __init__(self, team, ai_interface):
        self.team_ = team
        self.interface = ai_interface
        self.broad_ = {
            " PID ": self.brd_rcv_pid,
            " WELCOME": self.brd_rcv_welcome,
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
        self.mailBox = list()
        for char in self.interface.getTeamName():
            self.key_ += ord(char)

    # getter
    def getNumber(self):
        return self.number_

    def getMailBox(self):
        return self.mailBox

    # setter
    def setNumber(self, value):
        self.number_ = value

    # Methods
    def addMail(self, text):
        self.mailBox.append(text)

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

    def brd_snd_welcome(self):
        if str(self.lastpid_) == "":
            return
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " WELCOME "
        text += str(client.getPid()) + " " + str(self.lastpid_)

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)

    def brd_snd_inventory(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " INVENTORY "
        text += str(client.getPid()) + " " + str(client.getLvl())
        for key, val in client.getInventory().items():
            text += ''.join(' {} {}'.format(key, val))

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)

    def brd_snd_eat_on(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " EAT_ON "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)

    def brd_snd_eat_off(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " EAT_OFF "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)

    def brd_snd_grp_ritual(self):
        return

    def brd_snd_ab_ritual(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " AB_RITUAL "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)

    def brd_snd_str_ritual(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " STR_RITUAL "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)

    def brd_snd_end_ritual(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " END_RITUAL "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)

    def brd_snd_fork(self):
        client = self.team_.list_cli_[0]
        text = str(self.number_) + " FORK "
        text += str(client.getPid())

        text = self.stream_cipher(text)
        self.interface.broadcastAction(text)

    # rcv
    def brd_rcv_pid(self, text):
        return

    def brd_rcv_welcome(self, text):
        return

    def brd_rcv_inventory(self, text):
        return

    def brd_rcv_eat_on(self, text):
        return

    def brd_rcv_eat_off(self, text):
        return

    def brd_rcv_grp_ritual(self, text):
        return

    def brd_rcv_ab_ritual(self, text):
        return

    def brd_rcv_str_ritual(self, text):
        return

    def brd_rcv_end_ritual(self, text):
        return

    def brd_rcv_fork(self, text):
        return
