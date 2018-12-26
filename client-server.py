from flask import Flask, jsonify,Response
import requests
import random

app = Flask(__name__)
@app.route('/')
def datasearch():
  db = [
            {'name': 'Sandeep', 'age': 27, 'address': 'mazha'},
            {'name': 'steev', 'age': 24, 'address': 'grace' },
            {'name': 'Joice', 'age':25, 'address': 'rose villa'},
            {'name':'Nishanth','age':25, 'address':'fortuner'},
            {'name':'Nidheesh','age':30, 'address':'puzha'}
        ]
  
  d = (random.choice(db))
  print(d)
  return jsonify(d)







if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')


