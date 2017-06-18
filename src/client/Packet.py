
class Packet:

    def __init__(self, cmd, gui=False):
        self.cmd = cmd
        self.is_gui_packet = gui
        self.listeners = []

    def addListener(self):
        pass

    def removeListener(self):
        pass

    @staticmethod
    def parsePacket(raw):
        pass