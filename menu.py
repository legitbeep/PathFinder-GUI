from tkinter import *

class Menu():
	def __init__(self):
		self.active = 0
		self.state = False
		self.randomMaze = False

	def toggle(self,id,btn,pbtn):
		on = "#52C3CC"
		off = "#0E4448"
		if not self.state:
			self.state = True
			self.active = id
			btn.configure(bg = off)
			pbtn.configure(state=NORMAL)
		elif self.state:
			if self.active == id :
				self.state = False
				self.active = -1
				btn.configure(bg = on)
				pbtn.configure(state=DISABLED)

	def closeWindow(self,root):
		root.destroy()

	def help(self,root):


	    a=Tk()
	    a.geometry("300x500")
	    a.configure(bg="#232528")


	    b=Label(a,text="Help",font=("consolas bold",16),height=1,width=9,bg="#232528",fg="white",bd=0,padx=5,pady=5).place(x=100,y=0)

	    head1 = Label(a,text="Main Menu :",font=("consolas",14),bg="#232528",fg="white").place(x=100,y=30)
	    txt1 = Text(a,font=("consolas",12),bg="#232528",fg="white",height=3,width=33)
	    txt1.insert(END, "Here you have to select one \nalgorithm to solve the maze and  check the random maze if you wish not to make on yourself and press PROCEED.")
	    txt1.place(x=0,y=60)

	    txt1.configure(state=DISABLED)

	    head2 = Label(a,text="Random Maze :",font=("consolas",14),bg="#232528",fg="white").place(x=97,y=130)
	    txt2 = Text(a,font=("consolas",12),bg="#232528",fg="white",height=5,width=33)
	    txt2.insert(END,"If you selected random maze, then\nthe program will display a random maze withstart (orange) and end (pink) and start solving the maze instantly just wait and enjoy!")
	    txt2.place(x=0,y=160)
	    txt2.configure(state=DISABLED)

	    head3 = Label(a,text="Make Maze :",font=("consolas",14),bg="#232528",fg="white").place(x=97,y=263)
	    txt3 = Text(a,font=("consolas",12),bg="#232528",fg="white",height=9,width=33)
	    txt3.insert(END,"If you didn't select random maze,\nthen the program will ask you to\nmake a maze where the first left\nclick will make start (orange)\nand second will make end (pink) \npoints and the rest left click \nwill make walls , you can erase  walls with right click but not \nstart or end.")
	    txt3.place(x=0,y=300)

	    txt3.configure(state=DISABLED)


	    root.withdraw()
	    def back():
	    	root.deiconify()
	    	a.destroy()
	    back=Button(a,text="<<",width=5,pady=5,bg="#232528",fg="white",command=back).place(x=0,y=0)





	def randomToggle(self):
		if self.randomMaze:
			self.randomMaze = False
		else :
			self.randomMaze = True


	def createMenu(self):
		on = "#52C3CC"
		off = "#0E4448"
		root = Tk()
		root.title("Pathfinder")

		root.geometry("300x500")
		root.configure(bg="#232528")


		txt = Label(root,text="Main Menu",font=("consolas bold",16),height=1,width=9,bg="#232528",fg="white",bd=0,padx=100,pady=20).grid(row=0,column=0)

		btn1 = Button(root)
		btn2 = Button(root)
		btn3 = Button(root)
		btn4 = Button(root)
		pbtn = Button(root,text="PROCEED",width=44,pady=10,bg="#64EA4B",fg="black",activebackground="#319E1D",state=DISABLED,command = lambda:self.closeWindow(root))

		btns = []

		for i in range(1,5):
			btns.append(i)

		btn1.configure(text="A* Algorithm",width=44,pady=10,bg=on,fg="black",activebackground=off,command=lambda: self.toggle(btns[0],btn1,pbtn))
		btn1.place(x=0,y=100)
		btn2.configure(text="Djikstra's Algorithm",width=44,pady=10,bg=on,fg="black",activebackground=off,command=lambda: self.toggle(btns[1],btn2,pbtn))
		btn2.place(x=0,y=143)
		btn3.configure(text="Depth first search",width=44,pady=10,bg=on,fg="black",activebackground=off,command=lambda: self.toggle(btns[2],btn3,pbtn))
		btn3.place(x=0,y=186)
		btn4.configure(text="Breadth first search",width=44,pady=10,bg=on,fg="black",activebackground=off,command=lambda: self.toggle(btns[3],btn4,pbtn))
		btn4.place(x=0,y=229)

		random = Checkbutton(root,text="Random path",bg="#232528",fg="black",activebackground="#232528",font=("consolas",12),command = self.randomToggle)
		random.place(x=0,y=280)

		pbtn.place(x=0,y=350)

		btn5 = Button(root,text="Help",width=20,pady=10,bg="#E9AD80",fg="black",command=lambda : self.help(root))
		btn5.place(x=0,y=450)
		btn6 = Button(root,text="EXIT",width=20,pady=10,bg="#E9AD80",fg="black",command=quit)
		btn6.place(x=160,y=450)
		root.protocol("WM_DELETE_WINDOW",quit)
		root.resizable(False,False)
		root.mainloop()





