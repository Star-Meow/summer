from flask import Flask,render_template,request,jsonify
app = Flask(__name__)  #绑定app
 

@app.route('/') #路由
def index():
    return 'Hello World!'

@app.route('/NIUGET',methods=['GET']) #路由
def NIUGET():
    print('溫度:')
    print(request.args.get('temp'))
    print('濕度:')
    print(request.args.get('humid'))
    return ""
@app.route('/NIUPOST',methods=['POST']) #路由
def NIUPOST():
    print(request.headers)
    print(request.json)
    print('溫度:')
    print(request.json['temp'])
    print('濕度:')
    print(request.json['humid'])
    return ""

if __name__=='__main__':
    app.run(host='192.168.0.10', debug=False, threaded=True)
