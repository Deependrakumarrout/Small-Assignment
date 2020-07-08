
from tkinter import *

root=Tk()
data = Label(root,text="Hey python this is my first sentence that i am writing on it.\n"
                       "So think you will understand my felling to communicate ourselves")

data1 = Label(root,text="Ok lets see want happen next when i insert the row and column")

data.grid(row=0,column=0)
data1.grid(row=1,column=0)
#data.pack()
root.mainloop()

