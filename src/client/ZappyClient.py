from Network import *
from ai.AI import *
from gui.GUI import *
import sys
from Threading import *
from PacketRouter import *
from PacketParser import *

class ZappyClient:
    g_instance = None

    def isGraphical(self):
        return self.graphical

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
                    self.server_port = int(sys.argv[i + 1])
                elif arg == "-n":
                    self.team_name = sys.argv[i + 1]
                elif arg == "-h":
                    self.server_hostname = sys.argv[i + 1]
                elif arg == "-help":
                    sys.exit(ZappyClient.print_usage())
                elif arg == "-graphical":
                    self.graphical = True
            except IndexError:
                sys.exit(ZappyClient.print_usage())

        if self.server_port is None or self.team_name is None:
            sys.exit(ZappyClient.print_usage())

    def __init__(self):
        if not ZappyClient.g_instance is None:
            return
        ZappyClient.g_instance = self

        self.map_size = ()
        self.player_pos = ()
        self.server_hostname = "localhost"
        self.server_port = None
        self.team_name = None
        self.client_num = -1
        self.gui = GUI()
        self.ai = AI()
        self.graphical = False
        self.network = Network()
        self.packet_parser = PacketParser()
        self.packet_router = PacketRouter()
        self.running = True

        self.optparser()
        self.start()

    def start(self):
        self.optparser()
        self.network.connect_server()

        tp = ThreadPool(10)
        while self.running:
            try:
                try:
                    raw = self.network.recv_packet()
                except RuntimeError as msg:
                    print("Socket error : {}".format(msg))
                    sys.exit(1)
                tp.add_task(self.packet_router.route, raw)
            except KeyboardInterrupt:
                sys.exit(1)
        tp.wait_completion()