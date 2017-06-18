from Packet import *
#from ZappyClient import *
from Stack import *

class PacketRouter:

    def __init__(self):
        #self.zappy = ZappyClient.instance()
        self.pending_packets = Stack()
        self.packets = [
            Packet("WELCOME"),
            Packet("msz", gui=True),
            Packet("bct", gui=True),
            Packet("tna", gui=True),
            Packet("pnw", gui=True),
            Packet("ppo", gui=True),
            Packet("plv", gui=True),
            Packet("pin", gui=True),
            Packet("pex", gui=True),
            Packet("pbc", gui=True),
            Packet("pic", gui=True),
            Packet("pie", gui=True),
            Packet("pfk", gui=True),
            Packet("pdr", gui=True),
            Packet("pgt", gui=True),
            Packet("pdi", gui=True),
            Packet("enw", gui=True),
            Packet("eht", gui=True),
            Packet("ebo", gui=True),
            Packet("edi", gui=True),
            Packet("sgt", gui=True),
            Packet("seg", gui=True),
            Packet("smg", gui=True),
            Packet("suc", gui=True),
            Packet("sbp", gui=True)
        ]

    def route(self, raw):
        """
        if not self.zappy.isGraphical() and len(self.pending_packets) > 0:
            pass
        """
        for packet in self.packets:
            if raw[0:len(packet.cmd)] == packet.cmd:
                #if packet.is_gui_packet and not self.zappy.isGraphical():
                #    break
                print(raw)
                return True
        raise RuntimeError("Unknown packet : {}".format(raw))

    def getPacket(self, cmd):
        for (i, packet) in self.packets:
            print(packet)