import socket
import sys

ip = '127.0.0.1'

def manual():
	print("syntax: echoclient <host> <port>")
	sys.exit(0)

def main():
	if len(sys.argv) != 3:
		manual()
	
	host = sys.argv[1]
	port = int(sys.argv[2])
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	msg = raw_input("msg : ")
	s.send(msg.encode())
	
	data = s.recv(1024)
 	print(data.decode())
	s.close()

if __name__ == '__main__':
	main()