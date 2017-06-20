
class PacketParser:

    def __init__(self):
        from ZappyClient import ZappyClient
        self.zappy = ZappyClient.instance()

    def parseClientNumPacket(self, raw):
        pass

    def parseMapSizePacket(self, raw):
        data_splitted = raw.split(" ")
        if len(data_splitted) != 2:
            raise RuntimeError("Failed to parse map size")
        return (int(data_splitted[0]), int(data_splitted[1]))

    def parseLookPacket(self, packet, raw):
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
        return items

    def parseInventoryPacket(self, packet, raw):
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
        return inventory

    def parseMessagePacket(self, packet, raw):
        message_splitted = raw.split(", ")
        i = message_splitted[0].split(' ')[1]
        message = message_splitted[1][0:]
        return message

    def parseIncantationPacket(self, packet, raw):
        print("incantation: {}".format(raw))
        if raw == "ko":
            return raw
        elif raw == "Elevation underway":
            return "underway"
        elif raw.startswith("Current level"):
            return 1 #TODO
        else:
            raise RuntimeError("Failed to parse incantation packet")

    def parseConnectNbrPacket(self, packet, raw):
        return int(raw)