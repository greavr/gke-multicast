import socket
import os
import logging
import time


MCAST_GRP = os.environ.get("MCAST_GRP", '224.1.1.1')
MCAST_PORT = os.environ.get("MCAST_PORT", 5007)
# regarding socket.IP_MULTICAST_TTL
# ---------------------------------
# for all packets sent, after two hops on the network the packet will not 
# be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
MULTICAST_TTL = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

print(f"MCAST_GRP: {MCAST_GRP}")
print(f"MCAST_PORT: {MCAST_PORT}")
print(f"Socker IP: {socket.AF_INET}")

# For Python 3, change next line to 'sock.sendto(b"robot", ...' to avoid the
# "bytes-like object is required" msg (https://stackoverflow.com/a/42612820)
i = 0
msg = "robot"
while True:
    i += 1
    send_msg = msg + "-" + str(i)
    sock.sendto(send_msg.encode(), (MCAST_GRP, MCAST_PORT))
    print(f"Sending {send_msg}")
    time.sleep(1)
