from flask import Flask, render_template, jsonify
from recomienda import recomendaciones,alimentos, ejercicios 

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route("/alimentos/<tipo>")
def recomendarA(tipo):
    if(tipo=="perder"):
        return jsonify(recomendaciones["bajar_de_peso"]["alimentos_recomendados"])
    elif(tipo=='ganar'):
        return  jsonify(recomendaciones["ganar_masa_muscular"]["alimentos_recomendados"])
    else:
        return recomendaciones["mantener_estilo_de_vida_saludable"]["alimentos_recomendados"]

@app.route("/ejercicios/<tipo>")
def recomendarE(tipo):
    if(tipo=='perder'):
        return  jsonify(recomendaciones["bajar_de_peso"]["ejercicios_recomendados"])
    elif(tipo=='ganar'):
        return  jsonify(recomendaciones["ganar_masa_muscular"]["ejercicios_recomendados"])
    else:
        return  jsonify(recomendaciones["mantener_estilo_de_vida_saludable"]["ejercicios_recomendados"])

@app.route("/alimentos")
def all_alimentos():
    return jsonify(alimentos)
@app.route("/ejercicios")
def all_ejercicios():
    return jsonify(ejercicios)


app.run(host="0.0.0.0", debug=True, port=3000)
