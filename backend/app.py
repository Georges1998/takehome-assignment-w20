from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})

@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/shows", methods=['GET'])
def get_all_shows():
    return create_response({"shows": db.get('shows')})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


@app.route("/shows/<id>", methods=['GET'])
def getById(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    data = db.getById('shows', int(id))
    return create_response(data)

@app.route("/shows", methods=['POST'])
def create():
    newShow = {"name": request.args["param1"], "episodes_seen": request.args["param2"]}
    if request.args["param1"] == "" or request.args["param2"] == "":
     return create_response(status=404, message="One of the paramater is missing")
    else:
     db.create("shows",newShow)
     return create_response(message="Show Added")

@app.route("/shows/<id>", methods=['PUT'])
def updateShow(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    else:
        data = db.getById('shows',2)
        if request.args["param1"] != "":
            data['name']=request.args["param1"]
        if request.args["param2"] != "":
            data['episodes_seen']=request.args["param2"]
        return create_response(data)

@app.route("/shows/minepisodes/<num>", methods=['GET'])
def bonus(num):
    tvShows =  [i for i in db.get("shows") if i["episodes_seen"] > int(num)]
    return create_response({"shows": tvShows})

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""

if __name__ == "__main__":
    app.run(port=8080, debug=True)
