from Packet import *
from Stack import *
from PacketParser import *
from ai.AI import *
import queue

class PacketRouter:

    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()
        self.packet_i = 0
        self.pending_packets = queue.Queue()
        self.packets = [
            Packet(cmd="Forward",
                   parser=PacketParser.parseOkKoPacket,
                   listeners=[AI.onMovement]),
            Packet(cmd="Right",
                   parser=PacketParser.parseOkKoPacket,
                   listeners=[AI.onTurn]),
            Packet(cmd="Left",
                   parser=PacketParser.parseOkKoPacket,
                   listeners=[AI.onTurn]),
            Packet(cmd="Look",
                   parser=PacketParser.parseLookPacket,
                   listeners=[AI.onLookAroundResult]),
            Packet(cmd="Inventory",
                   parser=PacketParser.parseInventoryPacket,
                   listeners=[AI.onInventoryContent]),
            Packet(cmd="Connect_nbr",
                   parser=PacketParser.parseConnectNbrPacket,
                   listeners=[]),
            Packet(cmd="Fork",
                   parser=PacketParser.parseOkKoPacket,
                   listeners=[AI.onPlayerForked]),
            Packet(cmd="Eject",
                   parser=PacketParser.parseOkKoPacket,
                   listeners=[AI.onPlayerEject]),
            Packet(cmd="Take object",
                   parser=PacketParser.parseOkKoPacket,
                   listeners=[AI.onTakeObject]),
            Packet(cmd="Set object",
                   parser=PacketParser.parseOkKoPacket,
                   listeners=[]),
            Packet(cmd="Incantation",
                   parser=PacketParser.parseIncantationPacket,
                   listeners=[AI.onIncantationFinished]),
            Packet(cmd="dead",
                   listeners=[AI.onPlayerDead]),
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
        print("Client-num")

    def onMapSizePacket(self):
        AI.on_game_start()

    def route(self, raw):
        raw = raw[:-1]
        self.packet_i += 1
        if self.packet_i == 1:
            return self.onWelcomePacket()
        elif self.packet_i == 2:
            return PacketParser.parseClientNumPacket(raw)
        elif self.packet_i == 3:
            return PacketParser.parseMapSizePacket(raw)
        elif not self.pending_packets.empty():
            packet = self.pending_packets.get()
            packet.raw = raw
            if not packet.parser is None:
                return packet.parser(packet)
        for p in self.packets:
            if raw[0:len(p.cmd)] == p.cmd:
                return p.callListeners()
        raise RuntimeError("Unknown packet : {}".format(raw))

    def getPacket(self, cmd):
        for packet in self.packets:
            if packet.cmd == cmd:
                return packet
        raise RuntimeError("Packet '{}' not found".format(cmd))