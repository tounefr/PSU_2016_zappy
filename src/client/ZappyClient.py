from core.Network import *
import sys
from core.Threading import *
from core.PacketRouter import *
from core.PacketParser import *
from multiprocessing import Event

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
        return 1

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
        if not self.graphical:
            if self.team_name is None:
                sys.exit(ZappyClient.print_usage())

    def __init__(self):
        self.fork_cond = Event()
        if not ZappyClient.g_instance is None:
            return
        ZappyClient.g_instance = self
        self.running = True
        self.map_size = ()
        self.player_pos = ()
        self.server_hostname = "localhost"
        self.server_port = 4242
        self.team_name = ""
        self.client_num = -1
        self.graphical = False
        self.optparser()

        while self.running:
            try:
                pid = os.fork()
            except:
                sys.exit(1)

            if pid == 0:
                self.gui = GUI()
                self.ai = AI()
                self.network = Network()
                self.packet_parser = PacketParser()
                self.packet_router = PacketRouter()
                self.start()
                sys.exit(1)
            else:
                self.fork_cond.wait()
                self.fork_cond.clear()

    def startGUI(self):
        print("GRAPHIC")
        tp = ThreadPool(1)
        tp.add_task(self.gui.update)
        while self.running:
            try:
                try:
                    raw = self.network.recv_packet()
                except RuntimeError as msg:
                    print("Socket error : {}".format(msg))
                    sys.exit(1)
                self.packet_router.route(raw)
            except KeyboardInterrupt:
                sys.exit(1)
        tp.wait_completion()
        sys.exit(1)

    def startAI(self):
        print("AI")
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
        sys.exit(1)

    def start(self):
        try:
            self.network.connect_server()
        except RuntimeError:
            sys.exit(1)
        if self.graphical:
            return self.startGUI()
        return self.startAI()

if __name__ == "__main__":
    zappy = ZappyClient()