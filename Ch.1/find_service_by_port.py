#!/usr/bin/env

import socket


def find_service_name():
    protocol_name = 'tcp'

    for port in [20, 21, 22, 23, 80, 81, 443, 100]:
        print ("Port: %s => service: %s" % (port, socket.getservbyport(port, protocol_name)))

    print ("Port: %s => service name: %s" % (53, socket.getservbyport(53, 'udp')))


if __name__ == "__main__":
    find_service_name()