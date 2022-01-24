from flask import Flask, jsonify, make_response, request

from maze import mazes

app = Flask(__name__)
maze_collection = mazes.MazeCollection()


@app.route("/mazes", methods=["POST"])
def create_maze_endpoint():
    maze = request.json
    if not maze_collection.valid_maze(maze):
        return {"error": "invalid maze"}, 400

    maze_id = maze_collection.add_maze(maze)
    response = make_response({"id": maze_id, "content": maze}, 201)
    response.headers["Location"] = f"/mazes/{maze_id}"
    return response


@app.route("/mazes/<maze_id>/values", methods=["GET"])
def search_values_endpoint(maze_id):
    maze_id = int(maze_id)

    if maze_id not in maze_collection.mazes:
        return {"error": "maze not found"}, 404
    
    value, operator = request.args.get("value"), request.args.get("operator")
    
    if value is None or operator is None:
        return make_response(jsonify([]), 200)
    
    value = int(value)
    values = maze_collection.search(maze_id, value, operator)
    
    return make_response(jsonify(values), 200)
