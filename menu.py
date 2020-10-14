from tkinter import *

root = Tk()

root.geometry("300x500")
root.configure(bg="#232528")

txt = Text(root,font="consolas",height=1,width=9,bg="#232528",fg="white",bd=0,pady=20)
txt.pack()
txt.insert(END,"Main Menu")
txt.configure(state="disabled")

txt2 = Text(root,font="consolas",height=1,width=16,bg="#232528",fg="white",bd=0,pady=50)
txt2.pack()
txt2.insert(END,"Choose Algorithm")
txt2.configure(state="disabled")

btn1 = Button(root,text="A* Algorithm",width=44,pady=10,bg="#52C3CC",fg="black",activebackground="#0E4448").place(x=0,y=250)
btn2 = Button(root,text="Djikstra's Algorithm",width=44,pady=10,bg="#52C3CC",fg="black",activebackground="#0E4448").place(x=0,y=295)
btn2 = Button(root,text="Help",width=44,pady=10,bg="#52C3CC",fg="black",activebackground="#0E4448").place(x=0,y=340)
btn3 = Button(root,text="EXIT",width=44,pady=10,bg="#E9AD80",fg="black").place(x=0,y=450)

root.resizable(False,False)
mainloop()