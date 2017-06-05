import reed
import temperature
import sys
import time
import threading
temp = 2.1
from flask import Flask
import datetime

# Flask stuff

app = Flask(__name__)
@app.route("/user/<username>")
def show_user_profile(username): 
  return 'User %s' %username
@app.route('/post/<int:post_id>')
def show_post(post_id):
   return 'Post %d' %post_id

@app.route("/")
def index():
   return 'Index Page'
@app.route("/temp")
def hi():
   print(temp)
   return "Hola! La última temperatura en el servidor es: " +str(temp)

#Monitoring thread

class myThread (threading.Thread):
	def __init__(self, threadID, name,temp):
	   threading.Thread.__init__(self)
	   self.threadID = threadID
	   self.name = name
	def run(self):
           while(True):
              print("Monitoring thread says: ")
              reed.getStateReed()
              global temp
              temp =temperature.read_temp()
              print(temp)
              time.sleep(5)
def main():
    print("Principio del main thread")
    newthread = myThread(1, "Thread-monitor", temp)
    newthread.start()
    print("Final del main thread")
    print("Starting Flask server")
    app.run(host='0.0.0.0', port=8080, debug=True)

#Run main
if __name__ == "__main__":
    main()
