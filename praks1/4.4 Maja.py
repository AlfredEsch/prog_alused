from tkinter import *
raam = Tk()
raam.title ("Lipp")
tahvel = Canvas(raam, width=800, height= 800)



tahvel.create_rectangle(100,200,500,500, width=1, fill="lightgreen")
tahvel.create_oval(300,400,500,400, fill="lightblue")
tahvel.create_rectangle(250,350,350,500, width=1, fill="brown")
tahvel.create_oval(325,400,350,425, fill="gold")
tahvel.pack()
raam.mainloop()