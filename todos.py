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

@app.route("/todos", methods = ['POST'])
def addTodos():
    tarea = request.get_json()
    tareas.append(tarea)
    return tareas

app.run()
