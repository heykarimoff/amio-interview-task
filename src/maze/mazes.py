import itertools
import functools
import operator
from random import randint


class MazeCollection:
    OPERATORS = ["equal", "not_equal", "less_than", "greater_than", "less_than_or_equal", "greater_than_or_equal"]

    def __init__(self):
        self.mazes = {}

    def valid_maze(self, maze):
        if not isinstance(maze, list):
            return False
        return True

    def generate_maze_id(self):
        return randint(0, 1000000)

    def add_maze(self, maze):
        maze_id = self.generate_maze_id()
        self.mazes[maze_id] = maze
        return maze_id
    
    def get_maze(self, maze_id):
        return self.mazes[maze_id]

    def search(self, maze_id, value, operator):
        maze = self.get_maze(maze_id)
        result = list(filter(lambda x: self.evaluate(x, value, operator), self.traverse(maze)))
        return result
        
    def traverse(self, a):
        for item in a:
            if isinstance(item, int):
                yield item
            elif isinstance(item, list):
                yield from self.traverse(item)

    def evaluate(self, a, b, operator):
        if operator == "equal":
            return a == b
        elif operator == "not_equal":
            return a != b
        elif operator == "less_than":
            return a < b
        elif operator == "greater_than":
            return a > b
        elif operator == "less_than_or_equal":
            return a <= b
        elif operator == "greater_than_or_equal":
            return a >= b
        else:
            return False
