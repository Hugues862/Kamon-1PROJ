import pickle
import socket
import struct


def send_data(conn, data):
    size = len(data)
    size_in_4_bytes = struct.pack("I", size)
    conn.send(size_in_4_bytes)
    conn.send(data)


def recv_data(conn):
    size_in_4_bytes = conn.recv(4)
    size = struct.unpack("I", size_in_4_bytes)
    size = size[0]
    data = conn.recv(size)
    return data
