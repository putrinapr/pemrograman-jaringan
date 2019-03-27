import socket

def Main():
	IP = '127.0.0.1'
	PORT = 9000

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP, PORT))

	while True:
		file = raw_input("Input file: ")
		if file == 'quit':
			s.close()
			break

		elif file == 'list':
			s.send("list")
			userResponse = s.recv(1024)
			print str(userResponse)

		else:
			s.send(file)
	        data = s.recv(1024)

	        if data[:6] == 'EXISTS':
	            filesize = long(data[6:])
	            message = raw_input("Size of file: " + str(filesize) +"bytes // Download? (Y/N) ")
	            if message == 'Y':
	                s.send("OK")
	                f = open('new_'+file, 'wb')
	                data = s.recv(1024)
	                totalRecv = len(data)
	                f.write(data)
	                while totalRecv < filesize:
	                    data = s.recv(1024)
	                    totalRecv += len(data)
	                    f.write(data)
	                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% done"
	                    print "total: " + str(totalRecv)

	                print "Download finished"
	                f.close()
	        else:
	            print "File does not exist"


if __name__ == '__main__':
	Main()
