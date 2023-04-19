from flask import Flask, request, jsonify, render_template

app = Flask (__name__)

@app.route("/saludar", methods=['GET','POST'])
def saludar():
    if(request.method=='GET'):
        return "Buenas noches, hace frío :("
    else:
        body: request.get_json()
        print(body)
        # return f'buenas noches {body["name"]}, hace frio :('
        return jsonify({
            "name": body['name'],
            "saludo":"buenas noches, hace frio"
        })
@app.route('/', methods=['GET'])
def html():
    return render_template("index.html")
   
@app.route("/chayanne/<int:numero>", methods=['GET'])
def verso(numero):
    cancion = [
        "de lunes a domingo voy desesperado",
        "tu dime donde estas que yo no te he encontrado",
        "hay que ser torero, poner el alma enn el ruedo"
    ]
    return cancion[numero]


app.run(port='3452')