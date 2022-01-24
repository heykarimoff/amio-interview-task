from flask import Flask, jsonify, make_response, request

from maze import mazes

app = Flask(__name__)
maze_collection = mazes.MazeCollection()


@app.route("/v1/mazes", methods=["POST"])
def create_maze_endpoint():
    maze = request.json
    if not maze_collection.valid_maze(maze):
        return {"error": "invalid maze"}, 400

    maze_id = maze_collection.add_maze(maze)
    response = make_response({"id": maze_id, "content": maze}, 201)
    response.headers["Location"] = f"/mazes/{maze_id}"
    return response


@app.route("/v1/mazes/<maze_id>/values", methods=["GET"])
def search_values_endpoint(maze_id):
    try:
        maze_id = int(maze_id)
    except ValueError:
        return {"error": "invalid maze id"}, 400

    if maze_id not in maze_collection.mazes:
        return {"error": "maze not found"}, 404
    
    value, operator = request.args.get("value"), request.args.get("operator")
    
    if value is None or operator is None:
        return make_response(jsonify([]), 200)
    
    try:
        value = int(value)
    except ValueError:
        return {"error": "invalid value"}, 400
    
    if operator not in ["equal", "not_equal", "less_than", "greater_than", "less_than_or_equal", "greater_than_or_equal"]:
        return {"error": "invalid operator"}, 400
    
    result = maze_collection.search(maze_id, value, operator)
    return make_response(jsonify(result), 200)
