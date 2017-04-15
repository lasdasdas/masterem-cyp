#The program returns an array of options:
#	1 Returns the temperature on the sensor connected to the GPIO 
#	2 Returns the UNIX time of the server
#	3 Returns a signal to check ping
#	4 Returns the sum of two given numbers
#!/usr/bin/python3
import socket
import sys
import time
def client():
        # Check number of parameters
	if len (sys.argv) != 3:
		print('Usage: python3 client.py IP PORT')
		sys.exit(1)

	host = sys.argv[1]
	port = int(sys.argv[2])
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mySocket.connect((host,port))
	print("Press 1 for temperature\nPress 2 for ping\nPress 3 for time\nPress 4 for sum")
	option = input("Waiting for an option:   ")
	#After getting an option we check the time regardless the parameter is 2(Ping) for simplicity
	tic = time.time()
	mySocket.send(option.encode())
	if option =='1':
		data = mySocket.recv(1024).decode()
		print("The temperature is "+data)
	if option =='2':
		data = mySocket.recv(1024).decode()
		print("The UNIX time on the server is   "+data)	
	if option =='3':	
		data = mySocket.recv(1024).decode()	 	
		#If server returns OK we substract time since tic
		if data=='OK':
			toc=(time.time() - tic)*1000
			print("Connection latency: "+str(toc)+" ms")
		else:
			print("Error, did not get response, exiting")
	if option=='4':
		sum1=input("Enter sum number 1: " )
		mySocket.send(sum1.encode())
		sum2=input("Enter sum number 2: ")
		mySocket.send(sum2.encode())
		data = mySocket.recv(1024).decode()
		print ('Result received from server: ' + data)
	mySocket.close()
 
client()
