#! /usr/bin/python3
import os
from flask import Flask

app = Flask(__name__)

@app.get('/')
@app.get('/health')
def health():
   return " \
      OK \
      <h1>Author: <a href=/author>author</a></h1>\
      <h1>Hostname: <a href=/hostname>hostname</a></h1>\
      <h1>ID: <a href=/id>id</a></h1>"

@app.get('/hostname')
def hostname():
   return str(os.uname()[1])

@app.get('/author')
def author():
   return str(os.environ.get('AUTHOR'))

@app.get('/id')
def id():
   return str(os.environ.get('UUID'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)