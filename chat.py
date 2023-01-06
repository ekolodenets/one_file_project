import socket
import threading

choice = input('You are SERVER(1) or a CLIENT(2): ')

match choice:
    case '1':
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('192.168.200.168', 9999))
        server.listen()

        client, _ = server.accept()
    case '2':
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.200.168', 9999))
    case _:
        exit()

def sending_message(c):
    while True:
        message = input('')
        c.send(message.encode())
        print('You: ', message)


def receiving_message(c):
    while True:
        print('Partner: ', c.recv(1024).decode())

threading.Thread(target=sending_message, args=(client,)).start()
threading.Thread(target=receiving_message, args=(client,)).start()