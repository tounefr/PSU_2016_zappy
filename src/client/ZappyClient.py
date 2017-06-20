from Network import *
from PacketRouter import *
from ai.AI import *
from Inventory import *
from optparse import OptionParser

class ZappyClient:
    g_instance = None

    def isGraphical(self):
        return False

    @staticmethod
    def instance():
        return ZappyClient.g_instance

    def optparser(self):
        parser = OptionParser()
        parser.add_option("-p")
        (options, args) = parser.parse_args()
        print(options)
        print(args)

    def __init__(self):
        if not ZappyClient.g_instance is None:
            return
        ZappyClient.g_instance = self
        self.map_size = ()
        self.player_pos = ()
        self.team_name = "test1"
        self.network = Network()
        self.ai = AI()
        self.inventory = Inventory()
        self.running = True

    def entry_point(self):
        self.network.connect_server()
        while self.running:
            try:
                raw = self.network.recv_packet()
            except:
                break
            self.network.packet_router.route(raw)
        print("Disconnected")