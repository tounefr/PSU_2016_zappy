
class PacketParser:

    g_instance = None

    @staticmethod
    def instance():
        if PacketParser.g_instance is None:
            PacketParser.g_instance = PacketParser()
        return PacketParser.g_instance

    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()

    @staticmethod
    def parseClientNumPacket(raw):
        pass

    @staticmethod
    def parseMapSizePacket(raw):
        data_splitted = raw.split(" ")
        if len(data_splitted) != 2:
            raise RuntimeError("Failed to parse map size")
        PacketParser.instance().zappy.map_size = (int(data_splitted[0]), int(data_splitted[1]))
        PacketParser.instance().zappy.network.packet_router.onMapSizePacket()

    @staticmethod
    def parseOkKoPacket(packet, raw):
        if not raw in ["ok", "ko"]:
            raise RuntimeError("Failed to parse ok/ko response packet")
        if packet.cmd in ["Left", "Right"]:
            return packet.callListeners(direction=packet.cmd.lower())
        if packet.cmd == "Forward":
            return packet.callListeners()
        return packet.callListeners(res=raw)

    @staticmethod
    def parseLookPacket(packet, raw):
        error = "Failed to parse look packet"
        raw = raw.replace("[ ", "")
        raw = raw.replace(" ]", "")
        data_splitted = raw.split(", ")
        if len(data_splitted) < 2:
            raise RuntimeError(error)
        items = []
        for resource_count in data_splitted:
            resource_count_splitted = resource_count.split(" ")
            items.append(resource_count_splitted)
        packet.callListeners(items=items)

    @staticmethod
    def parseInventoryPacket(packet, raw):
        error = "Failed to parse inventory packet"
        data_splitted = raw.split(", ")
        if len(data_splitted) < 2:
            raise RuntimeError(error)
        data_splitted[0] = data_splitted[0].replace("[ ", "")
        data_splitted[-1] = data_splitted[-1].replace(" ]", "")
        inventory = {}
        for resource_count in data_splitted:
            resource_count_splitted = resource_count.split(" ")
            if len(resource_count_splitted) != 2:
                raise RuntimeError(error)
            inventory[resource_count_splitted[0]] = int(resource_count_splitted[1])
        packet.callListeners(inventory=inventory)

    @staticmethod
    def parseMessagePacket(packet, raw):
        message_splitted = raw.split(", ")
        i = message_splitted[0].split(' ')[1]
        message = message_splitted[1][0:]
        return packet.callListeners(i=i, msg=message)

    @staticmethod
    def parseIncantationPacket(packet, raw):
        if raw == "ko":
            return packet.callListeners(status="ko")
        elif raw == "Elevation underway":
            return packet.callListeners(status="underway")
        elif raw.startswith("Current level"):
            return packet.callListeners(status=1)
        else:
            raise RuntimeError("Failed to parse incantation packet")

    @staticmethod
    def parseConnectNbrPacket(raw):
        pass