import socket
import threading
import os

def RetrFile(name, sock):
	file = sock.recv(1024)

	if os.path.isfile(file):
		sock.send("EXISTS " + str(os.path.getsize(file)))
		userResponse = sock.recv(1024)

		if userResponse[:2] == 'OK':
			with open(file, 'rb') as f:
				bytesToSend = f.read(1024)
				sock.send(bytesToSend)
				while bytesToSend != "":
					bytesToSend = f.read(1024)
					sock.send(bytesToSend)
		else:
			sock.send("ERR")

		sock.close()

	#elif filename[:2] == 'up':
        #print "Uploading file..."
        #uploadResponse = sock.recv(1024)
        #if uploadResponse[:7] == "SENDING":
            #f = open('uploaded_' + file[9:], 'wb')
            #data = sock.recv(1024)
            #filesize = long(uploadResponse[8:])
            #totalRecv = len(data)
            #f.write(data)
            #while totalRecv < filesize:
                #data = sock.recv(1024)
                #totalRecv += len(data)
                #f.write(data)
                #print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"

            #print "Upload Complete!"
            #f.close()

	else:
		print "Error"

def Main():
	IP = '127.0.0.1'
	PORT = 9000

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((IP, PORT))

	s.listen(5)

	print "Server started"
	while True:
		c, addr = s.accept()
		print "Connected to " + str(addr)
		t = threading.Thread(target=RetrFile, args=("retrThread", c))
		t.start()

	s.close()

if __name__ == '__main__':
	Main()
