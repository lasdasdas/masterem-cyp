#Servidor que queda a la espera de que se conecte algún cliente,
#reciba dos sumandos, calcule el resultado y se lo envíe al cliente
#!/usr/bin/python3
import socket
import sys
import time
import threading
import copy
#import tempdavid

#This is needed for the temperature readings
#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'

threads=[] #Contains the threads



#Thread class

class myThread (threading.Thread):
	def __init__(self, threadID, name, conn):
	   threading.Thread.__init__(self)
	   self.threadID = threadID
	   self.name = name
	   self.conn = conn

	def run(self):
	  print ("Starting " + self.name)
	  self.dealrequest()
	  print ("Exiting " + self.name)
	def dealrequest(self):
		data1 = self.conn.recv(1024).decode()
		if not data1:
			return()
		if data1 =='1':
			#Getting the temperature in the sensor from the imported library
			#tempdavid.py which is a copy of temperature.py but stored in calc-socket
			print('Temperature requested  ')
			#temp =tempdavid.read_temp()
			self.conn.send(str(18.75).encode())
		if data1 =='2':
			#Returning the UNIX time stamp
			print('Time requested ')
			unixtime =int(time.time())
			self.conn.send(str(unixtime).encode())
		if data1 =='3':
			#Sending a simple signal to confirm the message has arrived
			print("Client requested ping   ")
			self.conn.send(str('OK').encode())
		if data1 =='4':
			print("Sum requested, listening for numbers  ")
	                    #Getting the first number
			sum1 = self.conn.recv(1024).decode()
			if not sum1:
				return()
			print ("Num1: " + str(sum1))
			#Waiting for the second number)
			sum2=self.conn.recv(1024).decode()
			if not sum2:
				return()
			print ("Num2: " + str(sum2))
			result = int(sum1) + int(sum2)
			print ("sending sum: " + str(result))
			#Sending the result
			self.conn.send(str(result).encode())
def server():
		# Check number of parameters
		if len (sys.argv) != 3:
			print('Usage: python3 server.py IP PORT')
			sys.exit(1)
		host = sys.argv[1]
		port = int(sys.argv[2])
		mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mySocket.bind((host,port))
		mySocket.listen(1)

		while True:
			conn, addr = mySocket.accept()
			print ("Connection from: " + str(addr))
			newthread = myThread(len(threads), "Thread-"+str(len(threads)),  conn)
			newthread.start()
			print("go!")
			# newthread.dealrequest()

			threads.append(newthread)



#Deals the request from the client.


#Define main
def main():
	server()
#Run main
if __name__ == "__main__":
    main()
