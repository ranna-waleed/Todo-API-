from flask import Flask, jsonify
from routes.todos import todos_bp  # Import the todos blueprint

app = Flask(__name__)

# Register the todos blueprint
app.register_blueprint(todos_bp, url_prefix="/todos")

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == "__main__":
    app.run(port=3000)
