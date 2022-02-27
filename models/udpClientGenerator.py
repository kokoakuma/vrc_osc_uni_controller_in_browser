import argparse

from pythonosc import udp_client

from . import constant

def UDPClientGenerator() -> udp_client.SimpleUDPClient:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default=constant.ADDRESS, help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=constant.PORT, help="The port the OSC server is listening on")
    args = parser.parse_args()
    return udp_client.SimpleUDPClient(args.ip, args.port)