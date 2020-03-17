import socket
import os
import subprocess

s = socket.socket()
host = input("Please insert IP: ")
port = input("Please insert port: ")
port = int(port)

s.connect((host,port))


while True:
    output_str = input("insert message: ")
    s.send(str.encode(output_str))

    data = s.recv(20480,)

    if len(data) >0:
        response = data[:].decode("utf-8")
        print(response)