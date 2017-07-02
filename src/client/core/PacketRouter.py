from core.Packet import *
from core.PacketParser import *
from ai.AI import *
import queue
import threading
from gui.GUI import *

"""
            Packet(cmd="Current level",
                   parser=self.zappy.packet_parser.parseIncantationPacket),
"""

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
                   parser=self.zappy.packet_parser.parseDeadPacket,
                   listeners=[self.zappy.ai.onPlayerDead]),
            Packet(cmd="Broadcast"),
            Packet(cmd="message",
                   parser=self.zappy.packet_parser.parseMessagePacket,
                   listeners=[self.zappy.ai.onMessage]),
            Packet(cmd="msz",
                   parser=self.zappy.packet_parser.parseGUIMapSizePacket,
                   listeners=[self.zappy.gui.onMapSize],
                   gui=True),
            Packet(cmd="bct",
                   parser=self.zappy.packet_parser.parseGUIMapCaseContentPacket,
                   listeners=[self.zappy.gui.onMapCaseContent],
                   gui=True),
            Packet(cmd="tna",
                   parser=self.zappy.packet_parser.parseGUITeamName,
                   listeners=[self.zappy.gui.onTeamName],
                   gui=True),
            Packet(cmd="pnw",
                   parser=self.zappy.packet_parser.parseGUIPlayerConnect,
                   listeners=[self.zappy.gui.onPlayerConnect],
                   gui=True),
            Packet(cmd="ppo",
                   parser=self.zappy.packet_parser.parseGUIPlayerPos,
                   listeners=[self.zappy.gui.onPlayerPos],
                   gui=True),
            Packet(cmd="plv",
                   parser=self.zappy.packet_parser.parseGUIPlayerLevel,
                   listeners=[self.zappy.gui.onPlayerLevel],
                   gui=True),
            Packet(cmd="pin",
                   parser=self.zappy.packet_parser.parseGUIPlayerInventory,
                   listeners=[self.zappy.gui.onPlayerInventory],
                   gui=True),
            Packet(cmd="pex",
                   parser=self.zappy.packet_parser.parseGUIPlayerNum,
                   listeners=[self.zappy.gui.onPlayerSlay],
                   gui=True),
            Packet(cmd="pbc",
                   parser=self.zappy.packet_parser.parseGUIPlayerBroadcast,
                   listeners=[self.zappy.gui.onPlayerBroadcast],
                   gui=True),
            Packet(cmd="pic",
                   parser=self.zappy.packet_parser.parseGUIFirstPlayerTriggerSpell,
                   listeners=[self.zappy.gui.onFirstPlayerTriggerSpell],
                   gui=True),
            Packet(cmd="pie",
                   parser=self.zappy.packet_parser.parseGUIEndSpell,
                   listeners=[self.zappy.gui.onEndSpell],
                   gui=True),
            Packet(cmd="pfk",
                   parser=self.zappy.packet_parser.parseGUIPlayerNum,
                   listeners=[self.zappy.gui.onPlayerLayEgg],
                   gui=True),
            Packet(cmd="pdr",
                   parser=self.zappy.packet_parser.parsePlayerResource,
                   listeners=[self.zappy.gui.onPlayerThrowResource],
                   gui=True),
            Packet(cmd="pgt",
                   parser=self.zappy.packet_parser.parsePlayerResource,
                   listeners=[self.zappy.gui.onPlayerTakeResource],
                   gui=True),
            Packet(cmd="pdi",
                   parser=self.zappy.packet_parser.parseGUIPlayerNum,
                   listeners=[self.zappy.gui.onPlayerDieOfHunger],
                   gui=True),
            Packet(cmd="enw",
                   parser=self.zappy.packet_parser.parseGUIlayerLaid,
                   listeners=[self.zappy.gui.onPlayerLaid],
                   gui=True),
            Packet(cmd="eht",
                   parser=self.zappy.packet_parser.parseGUIEggNum,
                   listeners=[self.zappy.gui.onEggHatch],
                   gui=True),
            Packet(cmd="ebo",
                   parser=self.zappy.packet_parser.parseGUIEggNum,
                   listeners=[self.zappy.gui.onEggDieOfHunger],
                   gui=True),
            Packet(cmd="edi",
                   parser=self.zappy.packet_parser.parseGUIEggNum,
                   listeners=[self.zappy.gui.onServerTimeUnit],
                   gui=True),
            Packet(cmd="sgt",
                   parser=self.zappy.packet_parser.parseGUIUnitTime,
                   listeners=[self.zappy.gui.onServerTimeUnitUpdated],
                   gui=True),
            Packet(cmd="seg",
                   parser=self.zappy.packet_parser.parseGUITeamName,
                   listeners=[self.zappy.gui.onEndGame],
                   gui=True),
            Packet(cmd="smg",
                   parser=self.zappy.packet_parser.parseGUIMessage,
                   listeners=[self.zappy.gui.onServerMessage],
                   gui=True),
            Packet(cmd="suc",
                   listeners=[self.zappy.gui.onWrongCommand],
                   gui=True),
            Packet(cmd="sbp",
                   listeners=[self.zappy.gui.onWrongCommandParameters],
                   gui=True)
        ]


    def onWelcomePacket(self):
        if self.zappy.isGraphical():
            self.zappy.network.send("GRAPHIC")
        else:
            self.zappy.network.send(self.zappy.team_name)

    def onGameStart(self):
        if self.zappy.isGraphical():
            self.zappy.gui.onGameStart()
        else:
            self.zappy.ai.onGameStart()

    def queuePacket(self, raw):
        pass

    def route(self, raw):
        raw = raw[:-1]
        self.packet_i += 1

        if self.packet_i == 1 or raw == "WELCOME":
            return self.onWelcomePacket()
        elif self.packet_i == 2 and not self.zappy.isGraphical():
            return self.zappy.packet_parser.parseClientNumPacket(raw)
        elif self.packet_i == 3 and not self.zappy.isGraphical():
            try:
                self.zappy.map_size = self.zappy.packet_parser.parseMapSizePacket(raw)
            except:
                pass
            return self.onGameStart()

        for p in self.packets:
            if not self.zappy.isGraphical() and p.gui:
                continue
            if raw[0:len(p.cmd)] == p.cmd:
                raw_parsed = None
                if p.parser:
                    raw_parsed = p.parser(p, raw)
                if not raw_parsed is None:
                    return p.callListeners(raw_parsed)
                return

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