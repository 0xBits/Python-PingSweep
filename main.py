#!/usr/bin/env python

import subprocess
import ipaddress

SaveFile = open("PingSweep.txt", "a")

alive = []
dead = []

NetworkSubnet = ipaddress.ip_network('192.168.0.0/24', strict=False)
for i in NetworkSubnet.hosts():
    i = str(i)
    ReturnedHostPing = subprocess.call(["ping", "-c1", "-n", "-i0.1", "-s0", "-W1", i])
    if ReturnedHostPing == 0:
        alive.append(i)
    else:
        dead.append(i)
for ip in alive:
    print(ip + " is alive")
    SaveFile.write("\n" + ip + " is alive")
for ip in dead:
    print(ip + " is not alive")
    SaveFile.write("\n" + ip + " is dead")