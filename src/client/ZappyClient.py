from Network import *
from PacketRouter import *
from ai.AI import *
from Inventory import *
from optparse import OptionParser
import sys
from Threading import *
import time

class ZappyClient:
    g_instance = None

    def isGraphical(self):
        return False

    @staticmethod
    def instance():
        if ZappyClient.g_instance is None:
            ZappyClient.g_instance = ZappyClient()
        return ZappyClient.g_instance

    @staticmethod
    def print_usage():
        print("USAGE: ./zappy_client -p port -n name -h machine")
        print("\tport    is the port number")
        print("\tname    is the name of the team")
        print("\tmachine is the name of the machine; localhost by default")

    def optparser(self):
        for i, arg in enumerate(sys.argv):
            try:
                if arg == "-p":
                    self.server_port = sys.argv[i + 1]
                elif arg == "-n":
                    self.team_name = sys.argv[i + 1]
                elif arg == "-help":
                    sys.exit(ZappyClient.print_usage())
            except IndexError:
                sys.exit(ZappyClient.print_usage())

    def __init__(self):
        if ZappyClient.g_instance is None:
            ZappyClient.g_instance = self
        else:
            raise RuntimeError("Singleton")
        self.optparser()

        self.map_size = ()
        self.player_pos = ()
        self.team_name = "test1"
        self.network = Network()
        self.ai = AI()
        self.inventory = Inventory()
        self.running = True

        self.start()

    def start(self):
        self.optparser()
        self.network.connect_server()

        tp = ThreadPool(10)
        while self.running:
            raw = self.network.recv_packet()
            tp.add_task(PacketRouter.route, raw)
        tp.wait_completion()