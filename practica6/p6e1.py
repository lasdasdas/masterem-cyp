from flask import Flask
import datetime

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
@app.route("/hi")
def hi():
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
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)


