#!/usr/bin/env python
import socket
myHostname = socket.gethostname()
UDP_IP = "0.0.0.0"
UDP_PORT = 55585

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
  data, addr = sock.recvfrom(1024)
  if data == b"Hello?":
    print("Got someone searching")
    sock.sendto(("Hello, i am " + myHostname).encode(), addr)