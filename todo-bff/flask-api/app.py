from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []


@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.json
    todos.append(data)
    return jsonify({"message": "Todo added successfully"})


@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    todos[todo_id] = data
    return jsonify({"message": "Todo updated successfully"})


@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    del todos[todo_id]
    return jsonify({"message": "Todo deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
