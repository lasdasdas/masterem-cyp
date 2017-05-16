from flask import Flask , render_template , request
import datetime
import RPi.GPIO as GPIO
import time
import logging
from logging.handlers import RotatingFileHandler
 
PIN_LED1=17
PIN_LED2=27
PIN_LED3=22

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

@app.route("/maqueta")
def hello1():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   return "Hello maqueta! Hora del servidor: " + timeString

@app.route("/maqueta1")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'Hello maqueta!',
      'time': timeString
      }
   return render_template('main.html', **templateData)
@app.route("/maqueta/pin/<int:pin>", methods=['GET'])
def getPin(pin):
   try:
      GPIO.setup(pin, GPIO.IN)
      if GPIO.input(pin) == True:
         return "Pin number " + str(pin) + " is high!"
      # COMPLETA CODIGO CASO else
      else:
         return "Pin number " + str(pin) + " is not high!"
   except:
      
      return "There was an error reading pin " + str(pin) + "."
    
@app.route("/maqueta/pin/<int:pin>", methods=['POST'])
def setPin(pin):
    
    value = request.form['value']
    app.logger.info("Requested value to "+str( value))
    app.logger.error("Porque si")
    # value puede ser 0 o 1 para establecerlo a bajo/alto
    try:
        GPIO.setup(pin, GPIO.OUT)
        if int(value) == 1:
            GPIO.output(pin, True)
        # COMPLETAR CODIGO CASO else
        if int(value) == 0:
            GPIO.output(pin, False)
        # COMPLETAR CODIGO CASO else


        return "OK"
    except:
        app.logger.error("El pin  "+str(pi)+" no se encontor pin")
        return "There was an error setting pin " + str(pin) + " to ." + str(value)


if __name__ == "__main__":
   formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
   handler = RotatingFileHandler('log-api-cpy.log', maxBytes=10000, backupCount=2)
   handler.setLevel(logging.INFO)
   handler.setFormatter(formatter)
   app.logger.addHandler(handler)
   # Run
   app.run(host='0.0.0.0', port=8080, debug=True)


