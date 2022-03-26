from flask import Flask,request,jsonify,render_template
import json
app = Flask(__name__, template_folder='.')

@app.route('/')
def raiz():
    return render_template('index.html')

@app.route('/times', methods=['GET','POST','PUT','DELETE','HEAD'])
def times():
    file = open('times.json')
    times = json.load(file)
    file.close()
    return jsonify(times)

@app.route('/placar', methods=['GET','POST','PUT','DELETE','HEAD'])
def placar():
    file = open('placar.json')
    placar = json.load(file)
    file.close()
    return jsonify(placar)

@app.route('/jogos', methods=['GET','POST','PUT','DELETE','HEAD'])
def jogos():
    file = open('jogos.json')
    jogos = json.load(file)
    file.close()
    return jsonify(jogos)

app.run(host="0.0.0.0", port=8000, debug=False)