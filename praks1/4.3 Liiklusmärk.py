from tkinter import *
raam = Tk()
raam.title ("Lipp")
tahvel = Canvas(raam, width=800, height= 800)

tahvel.create_oval(600,600,6000,6000, fill="red", outline="green")tahvel.create_rectangle(100,150,600,250, width=1, fill="black")
tahvel.create_rectangle(100,250,600,350, width=1, fill="white")
tahvel.pack()
raam.mainloop()
