from ctypes import *
from PacketRouter import *

class Network:

    def __init__(self):
        self.libnetwork = cdll.LoadLibrary("./libnetwork.so")
        self.packet_router = PacketRouter()
        self.fd = self.libnetwork.socket_init()

    def connect(self, hostname, port):
        hostname = hostname.encode()
        ip = c_char_p(self.libnetwork.resolve_hostname(c_char_p(hostname))).value
        port = c_ushort(port)
        return self.libnetwork.socket_connect(self.fd, c_char_p(ip), byref(port))

    def connect_server(self):
        hostname = "localhost"
        port = 4242
        if not self.connect(hostname, port):
            raise RuntimeError("Failed to connect to {}:{}".format(hostname, port))

    def recv_packet(self):
        raw = self.libnetwork.recv_packet(self.fd)
        if not raw:
            raise RuntimeError("Failed to recv packet")
        try:
            raw = c_char_p(raw).value.decode()
            print("Recv<< {}".format(raw[:-1]))
            return raw
        except:
            raise RuntimeError("Failed to decode packet")

    def send_packet(self, packet):
        self.packet_router.pending_packets.put(packet)
        self.send(packet.cmd)

    def send(self, raw):
        print("Send>> {}".format(raw))
        raw = "{}\n".format(raw)
        if not self.libnetwork.socket_send(self.fd, c_char_p(raw.encode())):
            raise RuntimeError("Failed to send packet : {}".format(raw))