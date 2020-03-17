import socket
import sys

#create a socket to connect two computer
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 3333
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


#Binding for socker and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port: " + str(port))

        s.bind((host,port))
        s.listen(5)  #try 5 times
    except socket.error as msg:
        print("Socket Binding error: " + str(msg) + "\n Retrying...")
        bind_socket()


#Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + "IP" + address[0] + "| Port" + str(address[1])) #kat [0] dah dlm string tp lam [1] x string
    send_commands(conn)
    conn.close()


#Send reply to client
def send_commands(conn):
    while True:
        client_message = str(conn.recv(20480),"utf-8")
        if client_message == "I am a Network Programmer":
            conn.send(str.encode("Yes, you are network programmer"))
            s.close()
        else:
            conn.send(str.encode("Wrong Input"))


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()