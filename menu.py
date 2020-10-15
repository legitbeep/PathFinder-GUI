from tkinter import *

root = Tk()
root.title("Pathfinder")

root.geometry("300x500")
root.configure(bg="#232528")


txt = Label(root,text="Main Menu",font="consolas",height=1,width=9,bg="#232528",fg="white",bd=0,padx=100,pady=20).grid(row=0,column=0)

'''def a_algorithm():
    a_algo=Toplevel(root)
    a_algo.title("Pathfinder->A* Algorithm")
    a_algo.geometry("200x200")

    # A Label widget to show in toplevel
    label= Label(a_algo,
          text ="This is a new window").pack()
    label.pack()
'''


btn1 = Button(root,text="A* Algorithm",width=44,pady=10,bg="#52C3CC",fg="black",activebackground="#0E4448").place(x=0,y=100)
btn2 = Button(root,text="Djikstra's Algorithm",width=44,pady=10,bg="#52C3CC",fg="black",activebackground="#0E4448").place(x=0,y=143)
btn3 = Button(root,text="Depth first search",width=44,pady=10,bg="#52C3CC",fg="black",activebackground="#0E4448").place(x=0,y=186)
btn4 = Button(root,text="Breadth first search",width=44,pady=10,bg="#52C3CC",fg="black",activebackground="#0E4448").place(x=0,y=229)
btn5 = Button(root,text="Help",width=20,pady=10,bg="#E9AD80",fg="black").place(x=0,y=450)
btn6 = Button(root,text="EXIT",width=20,pady=10,bg="#E9AD80",fg="black",command=quit).place(x=160,y=450)






root.resizable(False,False)
mainloop()





