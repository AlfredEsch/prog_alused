from tkinter import *
raam = Tk()
raam.title ("Lipp")
tahvel = Canvas(raam, width=800, height= 800)

tahvel.create_oval(10,10,700,700, fill="red")

tahvel.create_rectangle(100,400,600,300, width=1, fill="white")
tahvel.pack()
raam.mainloop()
