from flask import Flask, request, render_template,jsonify
#from configs import Config
from os import getpid
#config = Config()
#server,port = config.getUrlConnection()
clients = []
conexao = False
statusMessage = []
erro = 0

app = Flask(__name__,template_folder='.')

@app.route('/')
def raiz():
    return render_template('index.html')

@app.route('/infoClient',methods=['POST'])
def getInfo():
    info = request.json
    clients.append(info)
    return '[200]'

@app.route('/seeInfo')
def seeInfo():
    global clients
    return '''<h1>lista clientes {}</h1>'''.format(clients)

@app.route('/getInfo',methods=['GET'])
def sendInfo():
    global clients
    teste = clients
    clients = []
    return jsonify(teste)

@app.route('/setCon')
def setCon():
    global conexao
    conexao = request.args.get('status')
    return 'recebido'

@app.route('/getCon')
def getCon():
    global conexao
    if conexao:
        return 'True'
    else:
        return 'False'

@app.route('/setErro',methods=['GET'])
def setErro():
    global erro
    erro = request.args.get('failsNumbers')
    return 'recebido'

@app.route('/getWrongNumber')
def getWrongNumber():
    global erro
    numberErro = erro
    erro = 0
    return numberErro

app.run(host='0.0.0.0',port=8080,debug=False)
