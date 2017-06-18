from Network import *
from PacketRouter import *

class ZappyClient:
    g_instance = None

    @staticmethod
    def instance():
        if ZappyClient.g_instance == None:
            ZappyClient.g_instance = ZappyClient()
        return ZappyClient.g_instance

    def isGraphical(self):
        return True

    def __init__(self):
        self.network = Network()
        self.packet_router = PacketRouter()
        self.running = True

    def entry_point(self):
        self.network.connect_server()
        if self.isGraphical():
            self.network.send_packet("GRAPHIC")
        while self.running:
            raw = self.network.recv_packet()
            self.packet_router.route(raw)