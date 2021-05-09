from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')

def index():
    return "Streaming Status : Online | NiNj4 HAX"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()


