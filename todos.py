from flask import Flask, request

app = Flask (__name__)

tareas = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

@app.route("/todos", methods = ['GET','POST'])
def addTodos():
    
    if(request.method=="GET"):
        return tareas
    else:
        tarea = request.get_json()
        tareas.append(tarea)
        return tareas
    
@app.route("/todos/<int:numero>", methods=['GET'])
def tarea(numero):
    return tareas[numero]

app.run()
