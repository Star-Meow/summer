from flask import Flask,render_template,request,jsonify
import sqlite3
import paho.mqtt.publish as publish
import datetime
import demjson
DB_File = ""
app = Flask(__name__)  #绑定app

@app.route('/') #路由
def index():
    return 'Hello World!'
@app.route('/setT/') #路由
def setT():

	return jsonify(chart) #回傳JSON資料
@app.route('/relay/<VAL>')
def relay(VAL):
	print(VAL)
	return""
@app.route('/CHART')  #路由
def CHART():
    return render_template('CHART.html')

if __name__=='__main__':
    app.run(host='192.168.0.10', debug=False, threaded=True)
