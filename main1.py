from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id): #path parameter
    user_data={
        "user_id": user_id,
        "name": "dasha ",
        "email":"dasha@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"]= extra
    return jsonify(user_data), 200

#query parameter

#post
@app.route("/create-useer", methods=['POST'])
def create_user():
    data= request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)    