from ctypes import *
import queue
import threading
import sys

class Network:
    def __init__(self):
        from ZappyClient import ZappyClient
        try:
            self.libnetwork = cdll.LoadLibrary("./libnetwork.so")
        except OSError as m:
            print("{}".format(m))
            sys.exit(1)
        self.fd = self.libnetwork.socket_init()
        self.zappy = ZappyClient.instance()

    def connect(self, hostname, port):
        hostname = hostname.encode()
        resolved_hostname = self.libnetwork.resolve_hostname(c_char_p(hostname))
        if not resolved_hostname:
            return None
        ip = c_char_p(resolved_hostname).value
        port = c_ushort(port)
        return self.libnetwork.socket_connect(self.fd, c_char_p(ip), byref(port))

    def connect_server(self):
        hostname = self.zappy.server_hostname
        port = self.zappy.server_port
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

    def send_packet(self, raw):
        self.zappy.packet_router.pending_packets.put(raw)
        with self.zappy.packet_router.cond:
            self.send(raw)
            self.zappy.packet_router.cond.wait()
        return self.zappy.packet_router.res_packet

    def send(self, raw):
        print("Send>> {}".format(raw))
        raw = "{}\n".format(raw)
        if not self.libnetwork.socket_send(self.fd, c_char_p(raw.encode())):
            raise RuntimeError("Failed to send packet : {}".format(raw))