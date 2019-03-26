import socket

IP = "127.0.0.1"
PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("TRIG", (IP, PORT))

def getImage():
    received = 0
    while True:
        data, addr = sock.recvfrom(1024)
        if data[:4] == "NAME":
            print "\r Received {}" . format(str(data[5:]))
            fp = open(data[5:], "wb+")
        elif data[:4] == "FINISH":
            print "\r Finished"
            fp.close()
            received = 0
        elif data[:3] == "END":
            print "\r End"
            break
        else:
            fp.write(data)
            received += len(data)
            print "\r Received {} from {}" . format(str(received),addr[0])

while True:
    data, addr = sock.recvfrom(1024)
    if str(data) == "START":
        getImage()
    break
