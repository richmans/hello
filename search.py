#!/usr/bin/env python
import socket
myHostname = socket.gethostname()
UDP_IP = "0.0.0.0"
UDP_PORT = 55586

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
print("Sending broadcast: Hello?")
sock.sendto("Hello?", ("255.255.255.255", UDP_PORT - 1))
sock.settimeout(10)
while True:
  try:
    data, addr = sock.recvfrom(1024)
  except:
    break
  print("Got response from %s: %s " % (addr[0], data))
  