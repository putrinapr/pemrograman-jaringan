from threading import Thread
import socket
import os


IP = "127.0.0.1"
PORT = 9000
BUF = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
server_address = (IP, PORT)
sock.bind(server_address)
print "\r Starting listener. IP: {} // Port: {}" . format(IP, PORT)

images = ["1.png", "2.jpg", "3.png"]

def sendImage(CIP, CPORT):
    addr = (CIP, CPORT)
    sock.sendto("START", (addr))
    for img in images:
        image_size = os.stat(img).st_size
        sock.sendto("NAME {}" .format(img), (addr))

        file = open(img,'rb')
        image = file.read()
        block_size = 0
        for block in image:
            sock.sendto(block, (addr))
            block_size = block_size + 1
            print "\r {} of {} sent" . format(block_size, image_size)

    sock.sendto("FINISH", (addr))
    file.close()
    sock.sendto("END", (addr))



while True:
    data, addr = sock.recvfrom(BUF) # maximum size of data
    if str(data) == "TRIG":
        thread = Thread(target=sendImage, args=(addr))
        print "\r Incoming connection from {}" . format(addr[0])
        thread.start()
