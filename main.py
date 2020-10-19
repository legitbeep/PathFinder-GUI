from menu import *
from mainPygame import *

algo = { 1 : "A*",
		 2 : "Djikstra",
		 3 : "DFS",
		 4 : "BFS" }

obj = Menu()
obj.createMenu()

if not obj.randomMaze  :
	Maze()
