from Packet import *
from Stack import *
from PacketParser import *
from ai.AI import *
import queue
import threading

class PacketRouter:

    g_instance = None

    @staticmethod
    def instance():
        if PacketRouter.g_instance is None:
            PacketRouter.g_instance = PacketRouter()
        return PacketRouter.g_instance

    def __init__(self):
        print("new instance")
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()
        self.packet_i = 0
        self.cond = threading.Condition(threading.Lock())
        self.pending_packets = queue.Queue()
        self.res_packet = None
        self.packets = [
            Packet(cmd="Forward"),
            Packet(cmd="Right"),
            Packet(cmd="Left"),
            Packet(cmd="Look",
                   parser=PacketParser.parseLookPacket),
            Packet(cmd="Inventory",
                   parser=PacketParser.parseInventoryPacket),
            Packet(cmd="Connect_nbr",
                   parser=PacketParser.parseConnectNbrPacket),
            Packet(cmd="Fork"),
            Packet(cmd="Eject"),
            Packet(cmd="Take"),
            Packet(cmd="Set"),
            Packet(cmd="Incantation",
                   parser=PacketParser.parseIncantationPacket),
            Packet(cmd="dead",
                   listeners=[AI.onPlayerDead]),
            Packet(cmd="Broadcast"),
            Packet(cmd="message",
                   parser=PacketParser.parseMessagePacket,
                   listeners=[AI.onMessage]),
            Packet(cmd="msz",
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

    @staticmethod
    def route(raw):
        self = PacketRouter.instance()
        raw = raw[:-1]
        self.packet_i += 1

        if self.packet_i == 1:
            return self.onWelcomePacket()
        elif self.packet_i == 2:
            return PacketParser.parseClientNumPacket(raw)
        elif self.packet_i == 3:
            self.zappy.map_size = PacketParser.parseMapSizePacket(raw)
            return AI.on_game_start()

        for p in self.packets:
            if raw[0:len(p.cmd)] == p.cmd:
                raw_parsed = None
                if p.parser:
                    raw_parsed = p.parser(p, raw)
                    print("parsed: {}".format(raw_parsed))
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