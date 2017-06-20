
class Packet:

    def __init__(self, listeners=[], parser=None, cmd="", gui=False):
        self.cmd = cmd
        self.gui = gui
        self.parser = parser
        self.listeners = listeners

    def callListeners(self, *args):
        returnv = False
        for listener in self.listeners:
            returnv = listener(*args)
        return returnv

    def setParser(self, parser):
        self.parser = parser

    def addListener(self, callback):
        self.listeners.append(callback)

    def removeListener(self, callback):
        self.listeners.remove(callback)