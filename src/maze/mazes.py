import itertools
import functools
import operator
from random import randint


class MazeCollection:
    OPRETAROR_MAP = {
        "equals": lambda x, y: x == y,
        "not_equal": lambda x, y: x != y,
        "less_than": lambda x, y: x < y,
        "greater_than": lambda x, y: x > y,
        "less_than_or_equal": lambda x, y: x <= y,
        "greater_than_or_equal": lambda x, y: x >= y,
    }
    OPERATORS = OPRETAROR_MAP.keys()

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
        return self.OPRETAROR_MAP[operator](a, b)
