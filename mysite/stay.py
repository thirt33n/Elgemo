from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
#def home():
  #return "Now awake"

def run():
  app.run(host='0.0.0.0',port = 8080)

def stay_awake():
  T = Thread(target = run)
  T.start()