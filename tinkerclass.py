from tkinter import *
from menu import *
from tilesHandler import *
SIZE = 50
TSIZE = 15

def callthis(maze):

	root = Tk()

	c = Canvas(root,width = SIZE*TSIZE, height= SIZE*TSIZE,bd=0,highlightthickness=0)
	obj = Display(c,SIZE,TSIZE,maze)
	c.pack()

	root.mainloop()
