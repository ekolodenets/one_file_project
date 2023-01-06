import socket
import threading
import rsa

public_key, private_key = rsa.newkeys(1024)
public_partner = None

choice = input('You are SERVER(1) or a CLIENT(2): ')

match choice:
    case '1':
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('192.168.200.168', 9999)) # taken from ipconfig command
        server.listen()

        client, _ = server.accept()
        client.send(public_key.save_pkcs1('PEM'))
        public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    case '2':
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.200.168', 9999))
        public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
        client.send(public_key.save_pkcs1('PEM'))
    case _:
        exit()

def sending_message(c):
    print('Connection established...\nChat created...')
    while True:
        message = input('')
        c.send(rsa.encrypt(message.encode(), public_partner))
        print('You: ', message)


def receiving_message(c):
    while True:
        print('Partner: ', rsa.decrypt(c.recv(1024), private_key).decode())

threading.Thread(target=sending_message, args=(client,)).start()
threading.Thread(target=receiving_message, args=(client,)).start()