from menu import *
from mainPygame import *
from random_maze import *
from tilesHandler import *
from tinkerclass import *


algo = { 1 : "A*",
		 2 : "Djikstra",
		 3 : "DFS",
		 4 : "BFS" }

obj = Menu()
obj.createMenu()
maze = []

if not obj.randomMaze  :
	maze = Maze()
else:
	randomMazeObj = RandomMaze(SIZE)
	maze = randomMazeObj.randomMaze()

print("finish")
callthis(maze)
