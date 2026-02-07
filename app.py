from flask import Flask, request, jsonify 
"""here flask = creates app/server
reques= info about incoming hhtp request 
jsonify = converts python data into json """ 

app = Flask(__name__)
"""here app is my server object
Flask(__name__) name of myy current file or module
"""
#fake database 
notes=[]
next_id=1
""" notes=[ emty list ]
next_id=1 is a counter each notes get uniqye id """
# Route Home page 
@app.route("/", methods=["GET"])
def home():
    return "Notes API running"

"""herr @app.route is decorator it connects url to a function 
"/" means the home page 
methods=["get" ] only allow get requests
def home() runs whn we vist our url """

#create a note
@app.route("/notes", methods=["POST"])
def create_note():
#URL is /notes
#method is POST (used to create something)
#when a client sends a POST request to /notes, Flask runs create_note().
    global next_id
    data = request.get_json(silent=True) or {}
    text = data.get("text")
    if not text:
        return jsonify({"error": "Missing 'text'"}), 400
    note = {"id": next_id, "text": text}
    notes.append(note)
    next_id += 1
    return jsonify(note), 201
#route:list notes 
@app.route("/notes", methods=["GET"])
def list_notes():
    return jsonify(notes), 200
@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)
    if not note:
        return jsonify({"error": "Note not found"}), 404
    return jsonify(note), 200

# DELETE a note
@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    global notes
    before = len(notes)
    notes = [n for n in notes if n["id"] != note_id]
    if len(notes) == before:
        return jsonify({"error": "Note not found"}), 404
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)




