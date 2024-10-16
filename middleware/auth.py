from flask import request, jsonify

TOKEN = "mysecrettoken"
#token authentication check
#bearer :type of authentication error
def authentication_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401
