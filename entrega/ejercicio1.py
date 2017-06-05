import reed
import temperature
import sys
import time
import threading


class myThread (threading.Thread):
	def __init__(self, threadID, name):
	   threading.Thread.__init__(self)
	   self.threadID = threadID
	   self.name = name

	def run(self):
           while(True):
              reed.getStateReed()
              print(temperature.read_temp())
              time.sleep(5)
def main():
    print("Principio del main thread")
    newthread = myThread(1, "Thread-monitor")
    newthread.start()
    print("Final del main thread")
#Run main
if __name__ == "__main__":
    main()
