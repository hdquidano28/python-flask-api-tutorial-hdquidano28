from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
  {"label": "My first task", "done":False},
  {"label": "My second task", "done":True}
]

@app.route('/todos', methods=['GET'])

def todo():
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
  request_body = request.get_json(force=True)
  todos.append(request_body)
  request_text = jsonify(todos)
  return request_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  print("This is the position to delete", position)
  todos.pop(position)
  remove_text = jsonify(todos)
  return remove_text
  


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)