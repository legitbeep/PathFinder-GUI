from menu import *
from mainPygame import *
from random_maze import *

algo = { 1 : "A*",
		 2 : "Djikstra",
		 3 : "DFS",
		 4 : "BFS" }

obj = Menu()
obj.createMenu()

if not obj.randomMaze  :
	maze = Maze()
else:
	randomMazeObj = RandomMaze()
	maze = randomMazeObj.randomMaze()
	for m in maze :
		for c in m :
			print(c,end= ' ')
		print()

