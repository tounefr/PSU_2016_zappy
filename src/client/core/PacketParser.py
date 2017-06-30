import sys
from core.Util import *

class PacketParser:

    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()

    def parseClientNumPacket(self, raw):
        if raw == "ko":
            self.zappy.running = False
            return False
        if not Util.isNumeric(raw):
            return False
        self.zappy.client_num = int(raw)

    def parseMapSizePacket(self, raw):
        data_splitted = raw.split(" ")
        if len(data_splitted) != 2:
            raise RuntimeError("Failed to parse map size")
        return (int(data_splitted[0]), int(data_splitted[1]))

    def parseLookPacket(self, packet, raw):
        try:
            raw = raw.replace("[", "")
            raw = raw.replace("]", "")
            data_splitted = raw.split(",")
            if len(data_splitted) < 2:
                raise RuntimeError()
            items = []
            for resource_count in data_splitted:
                resource_count_splitted = resource_count.strip(" ").split(" ")
                items.append(resource_count_splitted)
            return items
        except:
            raise RuntimeError("Failed to parse look packet")

    def parseInventoryPacket(self, packet, raw):
        try:
            data_splitted = raw.split(", ")
            if len(data_splitted) < 2:
                raise RuntimeError()
            data_splitted[0] = data_splitted[0].replace("[", "")
            data_splitted[-1] = data_splitted[-1].replace("]", "")
            inventory = {}
            for resource_count in data_splitted:
                resource_count_splitted = resource_count.strip(" ").split(" ")
                if len(resource_count_splitted) != 2:
                    raise RuntimeError()
                inventory[resource_count_splitted[0]] = int(resource_count_splitted[1])
            return inventory
        except:
            raise RuntimeError("Failed to parse inventory packet")

    def parseDeadPacket(self, packet, raw):
        return {
            "status": raw
        }

    def parseMessagePacket(self, packet, raw):
        try:
            message_splitted = raw.split(", ")
            player_num = int(message_splitted[0].split(' ')[1])
            message = ", ".join(message_splitted[1:])
            return {
                "player_num": player_num,
                "message": message
            }
        except:
            raise RuntimeError("Failed to parse message packet")

    def parseIncantationPacket(self, packet, raw):
        try:
            status = None
            if raw == "ko":
                status = "ko"
            elif raw == "Elevation underway":
                status = "underway"
            elif raw.startswith("Current level"):
                status = int(raw[len("Current level: "):])
            else:
                raise RuntimeError()
            return status
        except:
            raise RuntimeError("Failed to parse level packet")


    def parseConnectNbrPacket(self, packet, raw):
        return int(raw)

    #msz
    def parseGUIMapSizePacket(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {"size": (int(splitted[0]), int(splitted[1]))}
        except:
            raise RuntimeError("Failed to parse map size packet")

    #bct
    # items: {'linemate': 0, 'deraumere': 0, 'food': 0, ...}
    def parseGUIMapCaseContentPacket(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            pos = (int(splitted[0]), int(splitted[1]))
            resources = {
                "food": int(splitted[2]),
                "linemate": int(splitted[3]),
                "deraumere": int(splitted[4]),
                "sibur": int(splitted[5]),
                "mendiane": int(splitted[6]),
                "phiras": int(splitted[7]),
                "thystame": int(splitted[8])
            }
            return {"pos": pos, "resources": resources}
        except:
            raise RuntimeError("Failed to parse map case content packet")

    def parseGUITeamName(self, packet, raw):
        return {"team_name": raw[4:]}

    def parseGUIPlayerConnect(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "player_num": int(splitted[0]),
                "pos": (int(splitted[1]), int(splitted[2])),
                "orientation": int(splitted[3]),
                "level": int(splitted[4]),
                "team_name": splitted[5]
            }
        except:
            raise RuntimeError("Failed to parse player connect packet")

    def parsePlayerResource(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            resources = ["food", "linemate", "deraumere",
                         "sibur", "mendiane", "phiras",
                         "thystame"]
            resource = resources[int(splitted[1])]
            return {
                "player_num": int(splitted[0]),
                "resource": resource
            }
        except:
            raise RuntimeError("Failed to parse player resource packet")

    def parseGUIPlayerPos(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "player_num": splitted[0],
                "pos": (int(splitted[1]), int(splitted[2])),
                "orientation": int(splitted[3])
            }
        except:
            raise RuntimeError("Failed to parse player pos packet")

    def parseGUIPlayerLevel(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "player_num": int(splitted[0]),
                "level": int(splitted[1])
            }
        except:
            raise RuntimeError("Failed to parse player level packet")

    def parseGUIPlayerInventory(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "player_num": int(splitted[0]),
                "pos": (int(splitted[1]), int(splitted[2])),
                "resources": {
                    "food": int(splitted[3]),
                    "linemate": int(splitted[4]),
                    "deraumere": int(splitted[5]),
                    "sibur": int(splitted[6]),
                    "mendiane": int(splitted[7]),
                    "phiras": int(splitted[8]),
                    "thystame": int(splitted[9])
                }
            }
        except:
            raise RuntimeError("Failed to parse player inventory packet")

    def parseGUIPlayerNum(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "player_num": int(splitted[0])
            }
        except:
            raise RuntimeError("Failed to parse player num packet")

    def parseGUIPlayerBroadcast(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "player_num": int(splitted[0]),
                "message": " ".join(splitted[1:])
            }
        except:
            raise RuntimeError("Failed to parse player broadcast packet")

    def parseGUIFirstPlayerTriggerSpell(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            players_num = map(int, splitted[3:])
            return {
                "pos": (int(splitted[0]), int(splitted[1])),
                "level": int(splitted[2]),
                "players_num": players_num
            }
        except:
            raise RuntimeError("Failed to parse player trigger spell packet")

    def parseGUIEndSpell(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "pos": (int(splitted[0]), int(splitted[1])),
                "result": splitted[2]
            }
        except:
            raise RuntimeError("Failed to parse end spell packet")

    def parseGUIPlayerNameResourceNum(self, packet, raw):
        pass

    def parseGUIlayerLaid(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "egg_num": int(splitted[0]),
                "player_num": int(splitted[1]),
                "pos": (int(splitted[2]), int(splitted[3]))
            }
        except:
            raise RuntimeError("Failed to parse layer laid packet")

    def parseGUIEggNum(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "egg_num": int(splitted[0])
            }
        except:
            raise RuntimeError("Failed to parse egg num packet")

    def parseGUIUnitTime(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "unit_time": int(splitted[0])
            }
        except:
            raise RuntimeError("Failed to parse unit time packet")

    def parseGUIMessage(self, packet, raw):
        try:
            splitted = raw[4:].split(' ')
            return {
                "message": " ".join(splitted[1:])
            }
        except:
            raise RuntimeError("Failed to parse message packet")