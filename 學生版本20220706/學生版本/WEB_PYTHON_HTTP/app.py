from flask import Flask,render_template,request,jsonify
app = Flask(__name__)  #绑定app
 

@app.route('/') #路由
def index():
    return 'Hello World!'

@app.route('/NIUGET',methods=['GET']) #路由
def NIUGET():
    return ""
@app.route('/NIUPOST',methods=['POST']) #路由
def NIUPOST():
    return ""
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)
