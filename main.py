from menu import *
from mainPygame import *
from random_maze import *
from tilesHandler import *
from solve import *

obj = Menu()
obj.createMenu()
maze = []

if not obj.randomMaze  :
	maze = Maze()
else:
	randomMazeObj = RandomMaze(SIZE)
	maze = randomMazeObj.randomMaze()

print("finish")
solveMaze(maze,obj.active)
