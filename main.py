from menu import *
from mainPygame import *
from random_maze import *
from tilesHandler import *

SIZE = 50
TSIZE = 15

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

root = Tk()

c = Canvas(root,width = SIZE*TSIZE, height= SIZE*TSIZE,bd=0,highlightthickness=0)
obj = Display(c,SIZE,TSIZE,maze)
c.pack()

root.mainloop()

