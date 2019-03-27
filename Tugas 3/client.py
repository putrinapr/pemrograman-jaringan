import socket

def Main():
	IP = '127.0.0.1'
	PORT = 9000

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP, PORT))

	while True:
		print "Commands:"
		print "1. <file name> - download file"
		print "2. <folder>/<file name> - download file in folder"
		print "3. up <file name> - upload file"
		print "4. quit - close app"

		file = raw_input("Input command: ")
		if file == 'quit':
			s.close()
			break

		else:
			s.send(file)
	        data = s.recv(1024)

	        if data[:6] == 'EXISTS':
	            filesize = long(data[6:])
	            message = raw_input("Size of file: " + str(filesize) +"bytes // Would you like to download? (Answer: Yes/No) ")
	            if message == 'Yes':
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
