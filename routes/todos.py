from flask import Blueprint, request, jsonify
from middleware.auth import authentication_token  # Import the auth middleware

todos_bp = Blueprint('todos', __name__)

todos = []

@todos_bp.before_request
def before_request():
    return authentication_token()

# GET /todos - Fetch all todos
@todos_bp.route("/", methods=["GET"])
def get_todos():
    return jsonify(todos)

# POST /todos - Create a new todo
@todos_bp.route("/", methods=["POST"])
def create_todo():
    todo = {
        "id": len(todos) + 1,
        "title": request.json.get("title"),
        "completed": request.json.get("completed", False),
    }
    todos.append(todo)
    return jsonify(todo), 201

# PUT /todos/<id> - Update an existing todo
@todos_bp.route("/<int:id>", methods=["PUT"])
def update_todo(id):
    todo = next((t for t in todos if t["id"] == id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    todo["title"] = request.json.get("title", todo["title"])
    todo["completed"] = request.json.get("completed", todo["completed"])
    return jsonify(todo)

# DELETE /todos/<id> - Delete a todo
@todos_bp.route("/<int:id>", methods=["DELETE"])
def delete_todo(id):
    global todos
    todos = [t for t in todos if t["id"] != id]
    return '', 204

# GET /todos/<id> - Get a specific todo by id
@todos_bp.route("/<int:id>", methods=["GET"])
def get_todo(id):
    todo = next((t for t in todos if t["id"] == id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo)
