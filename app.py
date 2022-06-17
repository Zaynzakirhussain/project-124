from flask import Flask,jsonify,request

app = Flask(__name__)

#create an array of tasks with each task as a differrent object in it.
contacts = [
    {
        'id' : 1,
        'Name' : "Dad",
        'Contact' : "9158368108",
        'done' : False
    },
    {
        'id' : 2,
        'Name' : "Mom",
        'Contact' : "9880370510",
        'done' : False
    }
] 

@app.route("/add-data", methods = ["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "please provide data!"
        },400)

    contact = {
        'id' : contacts[-1]['id']+1,
        'Name' : request.json['Contact'],
        'Contact' : request.json.get('description',"Contact"),
        'done' : False
    }
    contacts.append(contact)
    return jsonify({
        "status" : "success",
        "message" : "contact added successfully!"
    })

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data" : contacts
    })

if __name__ == '__main__':
    app.run(debug = True)