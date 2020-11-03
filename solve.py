from tkinter import *
from menu import *
from tilesHandler import *
from algorithms import *

import multiprocessing
multiprocessing.set_start_method('spawn')
from multiprocessing import Process


SIZE = 50
TSIZE = 15
recolor = "#00FF82"
border = "#38B8BB"
ALGO = { 1 : "A* Algorithm",
		 2 : "Djikstra Algorithm",
		 3 : "DFS Algorithm",
		 4 : "BFS Algorithm" }
def runAlgo(choice,Dobj):

	algorithm = algo()

	if ALGO[choice] == "A* Algorithm":
		cf,cc,done,bn = algorithm.aStar(Dobj.start,Dobj.end)

		if done :
			path = Dobj.constructPath(cf,Dobj.start,Dobj.end)
		else :
			return 0	

		cost = cc[Dobj.end]
		print("Total cost ",cost)
	elif ALGO[choice] == "Djikstra Algorithm":
		cf,cc,done,bn = algorithm.djikstra(Dobj.start,Dobj.end)

		if done :
			path = Dobj.constructPath(cf,Dobj.start,Dobj.end)
		else :
			return 0

		cost = cc[Dobj.end]
		print("Total cost ",cost)

	elif ALGO[choice] == "DFS Algorithm":
		cf,done,bn = algorithm.dfs(Dobj.start,Dobj.end)
		if done :
			path = Dobj.constructPath(cf,Dobj.start,Dobj.end)
		else :
			return 0
		cost = 0
		for tile in path:
			cost += tile.weight
		print("Total cost ",cost)

	elif ALGO[choice] == "BFS Algorithm":
		cf,done,bn = algorithm.bfs(Dobj.start,Dobj.end)

		if done :	
			path = Dobj.constructPath(cf,Dobj.start,Dobj.end)
		else :
			return 0

		cost = 0 
		
		for tile in path:
			cost += tile.weight
		print("Total cost ",cost)

	if done :
		processes =  []
		for tile,cameFrom in cf.items():
			if cameFrom is None:
				pass
			else:
				if tile.val == 'E':
					break
				if tile.val != 'S' and tile.val != 'E' and not tile.visited:
					pass
				else:
					processes.append(Process(target = Dobj.canvas.after, args=(25,Dobj.redrawTile(tile,tile.visitedColor,border),)))

		for i in processes:
			try:
				i.start()
			except:
				break
			try:
				i.join()
			except:
				break


		processes = []
		for tile in bn : 
			if tile.val != 'S' and tile.val != 'E' and not tile.visited :
				processes.append(Process(target = Dobj.canvas.after, args=(25,Dobj.redrawTile(tile,"#00CFFF",border),)))
			elif tile.val == 'E':
				break;	
				
		for i in processes:
			try:
				i.start()
			except:
				break
			try:
				i.join()
			except:
				break

		processes = [] 
		for tile in path:
			processes.append(Process(target = Dobj.canvas.after, args=(25,Dobj.redrawTile(tile,recolor,border),)))

		for i in processes:
			try:
				i.start()
			except:
				break
			try:
				i.join()
			except:
				break

	
	return cost

def solveMaze(maze,choice):
	root = Tk()
	root.title(ALGO[choice])
	c = Canvas(root,width = SIZE*TSIZE, height= SIZE*TSIZE,bd=0,highlightthickness=0)
	Dobj = Display(c,SIZE,TSIZE,maze)
	c.pack()

	cost = runAlgo(choice,Dobj)

	root.resizable(False,False)
	root.mainloop()
