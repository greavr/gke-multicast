import socket
import struct
import os
import logging
from datetime import datetime


MCAST_GRP = os.environ.get("MCAST_GRP", '224.1.1.1')
MCAST_PORT = os.environ.get("MCAST_PORT", 5007)
IS_ALL_GROUPS = True


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if IS_ALL_GROUPS:
    # on this port, receives ALL multicast groups
    sock.bind(('', MCAST_PORT))
else:
    # on this port, listen ONLY to MCAST_GRP
    sock.bind((MCAST_GRP, MCAST_PORT))

logging.info("MCAST_GRP: {MCAST_GRP}")
logging.info("MCAST_PORT: {MCAST_PORT}")
logging.info("Socker IP: {socket.AF_INET}")

mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
  # For Python 3, change next line to "print(sock.recv(10240))"
  print(f"{sock.recv(10240)} - {datetime.now()}")