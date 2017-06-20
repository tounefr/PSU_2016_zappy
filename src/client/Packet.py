
class Packet:

    def __init__(self, listeners=[], parser=None, cmd="", gui=False, is_ko=False, is_ok=False, raw=""):
        self.cmd = cmd
        self.gui = gui
        self.is_ko = is_ko
        self.is_ok = is_ok
        self.parser = parser
        self.raw = raw
        self.listeners = listeners

    def callListeners(self, *args):
        returnv = False
        for listener in self.listeners:
            returnv = listener(*args)
        return returnv

    def addListener(self, callback):
        self.listeners.append(callback)

    def removeListener(self, callback):
        self.listeners.remove(callback)

    @staticmethod
    def parsePacket(raw):
        pass
        """
        if len(raw) <= 0 or raw[-1] != "\n":
            raise RuntimeError("Not a Zappy packet")
        raw = raw[:-1]
        is_ko = raw == "ko"
        is_ok = raw == "ok"
        packet = Packet(raw=raw, is_ko=is_ko, is_ok=is_ok)
        return packet
        """

    @staticmethod
    def forgePacket(**kwargs):
        pass