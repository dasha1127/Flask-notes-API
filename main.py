#we are gonna use flask its a micro web framework
from flask import Flask, request, jsonify

app= Flask(__name__)
# we need to create an root which is like an end point location on our api
@app.route("/")
def home():
    return "Home"
"""http methods: get(request data from a specified resource ),
post(create a resource ),put(update a resource ),delete """

if __name__ == "__main__":
    app.run(debug=True)