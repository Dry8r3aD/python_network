#!/usr/bin/env python

import socket
from binascii import hexlify


def convert_ipv4_address():
    for ip_addr in ['127.0.0.1', '8.8.8.8', '192.168.1.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)

        # 아래 출력을 할 때, Packed와 변수 사이에 이상한 값이 붙는다... 왜지...?
        print("IP Address: %s => Packed: %s, Unpacked: %s" % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

if __name__ == "__main__":
    convert_ipv4_address()