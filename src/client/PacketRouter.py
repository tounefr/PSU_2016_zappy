from Packet import *
from PacketParser import *
from ai.AI import *
import queue
import threading
from gui.GUI import *

class PacketRouter:

    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()
        self.network = self.zappy.network
        self.packet_i = 0
        self.cond = threading.Condition(threading.Lock())
        self.pending_packets = queue.Queue()
        self.res_packet = None

        self.packets = [
            Packet(cmd="Forward"),
            Packet(cmd="Right"),
            Packet(cmd="Left"),
            Packet(cmd="Look",
                   parser=self.zappy.packet_parser.parseLookPacket),
            Packet(cmd="Inventory",
                   parser=self.zappy.packet_parser.parseInventoryPacket),
            Packet(cmd="Connect_nbr",
                   parser=self.zappy.packet_parser.parseConnectNbrPacket),
            Packet(cmd="Fork"),
            Packet(cmd="Eject"),
            Packet(cmd="Take"),
            Packet(cmd="Set"),
            Packet(cmd="Incantation",
                   parser=self.zappy.packet_parser.parseIncantationPacket),
            Packet(cmd="dead",
                   listeners=[self.zappy.ai.onPlayerDead]),
            Packet(cmd="Broadcast"),
            Packet(cmd="message",
                   parser=self.zappy.packet_parser.parseMessagePacket,
                   listeners=[self.zappy.ai.onMessage]),
            Packet(cmd="msz",
                   listeners=[],
                   gui=True),
            Packet(cmd="bct",
                   gui=True),
            Packet(cmd="tna",
                   gui=True),
            Packet(cmd="pnw",
                   gui=True),
            Packet(cmd="ppo",
                   gui=True),
            Packet(cmd="plv",
                   gui=True),
            Packet(cmd="pin",
                   gui=True),
            Packet(cmd="pex",
                   gui=True),
            Packet(cmd="pbc",
                   gui=True),
            Packet(cmd="pic",
                   gui=True),
            Packet(cmd="pie",
                   gui=True),
            Packet(cmd="pfk",
                   gui=True),
            Packet(cmd="pdr",
                   gui=True),
            Packet(cmd="pgt",
                   gui=True),
            Packet(cmd="pdi",
                   gui=True),
            Packet(cmd="enw",
                   gui=True),
            Packet(cmd="eht",
                   gui=True),
            Packet(cmd="ebo",
                   gui=True),
            Packet(cmd="edi",
                   gui=True),
            Packet(cmd="sgt",
                   gui=True),
            Packet(cmd="seg",
                   gui=True),
            Packet(cmd="smg",
                   gui=True),
            Packet(cmd="suc",
                   gui=True),
            Packet(cmd="sbp",
                   gui=True),
        ]


    def onWelcomePacket(self):
        if self.zappy.isGraphical():
            self.zappy.network.send("GRAPHIC")
        else:
            self.zappy.network.send(self.zappy.team_name)

    def onClientNumPacket(self):
        pass

    def onGameStart(self):
        if self.zappy.isGraphical():
            self.zappy.gui.onGameStart()
        else:
            self.zappy.ai.onGameStart()

    def route(self, raw):
        raw = raw[:-1]
        self.packet_i += 1

        if self.packet_i == 1:
            return self.onWelcomePacket()
        elif self.packet_i == 2:
            return self.zappy.packet_parser.parseClientNumPacket(raw)
        elif self.packet_i == 3:
            if not self.zappy.isGraphical():
                self.zappy.map_size = self.zappy.packet_parser.parseMapSizePacket(raw)
            return self.onGameStart()

        for p in self.packets:
            if raw[0:len(p.cmd)] == p.cmd:
                raw_parsed = None
                if p.parser:
                    raw_parsed = p.parser(p, raw)
                return p.callListeners(p, raw_parsed)

        if not self.pending_packets.empty():
            packet = self.getPacket(self.pending_packets.get())
            self.res_packet = raw
            if packet.parser:
                self.res_packet = packet.parser(packet, raw)
            with self.cond:
                self.cond.notify()
            return

        raise RuntimeError("Unknown packet : {}".format(raw))

    def getPacket(self, cmd):
        for packet in self.packets:
            if cmd.startswith(packet.cmd):
                return packet
        raise RuntimeError("Packet '{}' not found".format(cmd))