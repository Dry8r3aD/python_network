#!/usr/bin/env python

import socket


def print_machine_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Hostname : %s" % hostname)
    print("IP Address : %s" % ip_address)

if __name__ == '__main__':
    print_machine_network_info()
