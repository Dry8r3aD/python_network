#!/usr/bin/env python

import socket


def get_remote_machine_info():
    remotehost = "nas.dry8r3ad.com"

    try:
        print("IP of %s : %s" % (remotehost, socket.gethostbyname(remotehost)))
    except socket.error as err_msg:
        print("%s: %s" % (remotehost, err_msg))


if __name__ == "__main__":
    get_remote_machine_info()