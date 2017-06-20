
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