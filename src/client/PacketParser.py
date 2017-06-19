
class PacketParser:

    @staticmethod
    def parseClientNumPacket(raw):
        pass

    @staticmethod
    def parseMapSizePacket(raw):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

        data_splitted = raw.split(" ")
        if len(data_splitted) != 2:
            raise RuntimeError("Failed to parse map size")
        zappy.map_size = (int(data_splitted[0]), int(data_splitted[1]))
        zappy.network.packet_router.onMapSizePacket()

    @staticmethod
    def parseOkKoPacket(packet):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

        if not packet.raw in ["ok", "ko"]:
            raise RuntimeError("Failed to parse ok/ko response packet")
        if packet.cmd in ["Forward", "Left", "Right"]:
            return packet.callListeners(direction=packet.cmd.lower(), res=packet.raw)
        return packet.callListeners(res=packet.raw)

    @staticmethod
    def parseLookPacket(packet):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

        error = "Failed to parse look packet"
        raw = packet.raw
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
    def parseInventoryPacket(packet):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

        error = "Failed to parse inventory packet"
        data_splitted = packet.raw.split(", ")
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
    def parseBroadcastPacket(packet):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

    @staticmethod
    def parseIncantationPacket(packet):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()

    @staticmethod
    def parseConnectNbrPacket(packet):
        from ZappyClient import ZappyClient
        zappy = ZappyClient.instance()
