from flask import Flask,render_template,request, jsonify,Response
from bson.objectid import ObjectId
from json import dumps
from flask_mysqldb import MySQL
import yaml
import requests
import re
from ser1 import db as qq
import random


app = Flask(__name__)
mysql = MySQL(app)
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']


@app.route('/',methods = ['GET'])
def samplefunction(): 
    #access your DB get your results here
   r = requests.get(url ="http://localhost:5000/")
   data = r.json()
   name = data['name']
   age = data['age']
   address = data['address']
   print(data['name'])
    #if request.method == 'POST':
   cur = mysql.connection.cursor()
   cur.execute("INSERT INTO person_data(name,age,address) VALUES(%s,%s,%s)",(name,age,address))
   mysql.connection.commit()
   cur.close()
   val= Response(dumps(data))
   val.headers['Access-Control-Allow-Origin'] = '*'
   return (val)



@app.route('/search', methods=['GET'])
def get_name():
    #print(random.choice(db))     

    name= str(request.args.get('q'))
    rsp = Response("not found", status=404)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    #if name == "":
        #return 
    result = []
    cur = mysql.connection.cursor()
    resultValue=cur.execute("SELECT * FROM person_data")
    table = cur.fetchall()
    for d in table:
        
        if re.match(str(name), d[0], flags=re.IGNORECASE):
            result.append({'name':d[0],'age':d[1],'address':d[2]})
            #print(result)

    

    if len(result) > 0:    
        resp = Response(dumps(result))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp    
    return rsp


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0',port ='5001')


