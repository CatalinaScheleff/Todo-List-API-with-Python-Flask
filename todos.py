from flask import Flask, request, jsonify

app = Flask (__name__)

todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

@app.route("/todos", methods = ['GET'])
def getTodos():
    return jsonify(todos)
   
    
@app.route("/todos", methods = ['POST'])
def addTodos():
    task = request.get_json()
    todos.append(task)
    return todos
    
@app.route("/todos/<int:index>", methods=['DELETE'])
def deleteTodos(index):
    todos.pop(index)
    return jsonify(todos)

app.run()
