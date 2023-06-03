#
# ./www/__init__.py
#
from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Home" 

# curl https://devops.alwaysdata.net/flask/get-user/123?extra=hello 
@app.route("/get-user/<user_id>")
def get_user(user_id):
    
    user_data = {
    "user_id": user_id,
    "name": "Jean Martin",
    "email": "jean.martin@free.fr"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

#  curl --header "Content-Type:application/json" --data '{"u":"123"}' -X POST http://devops.alwaysdata.net/flask/create-user

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":
  app.run(debug=True)

