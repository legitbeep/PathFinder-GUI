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


		txt = Label(root,text="Main Menu",font="consolas",height=1,width=9,bg="#232528",fg="white",bd=0,padx=100,pady=20).grid(row=0,column=0)

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

		btn5 = Button(root,text="Help",width=20,pady=10,bg="#E9AD80",fg="black")
		btn5.place(x=0,y=450)
		btn6 = Button(root,text="EXIT",width=20,pady=10,bg="#E9AD80",fg="black",command=quit)
		btn6.place(x=160,y=450)
		root.protocol("WM_DELETE_WINDOW",quit)
		root.resizable(False,False)
		root.mainloop()





