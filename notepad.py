from tkinter import*
from tkinter import scrolledtext

root = Tk()
root.title("Notepad")
txt = scrolledtext.ScrolledText(root,font ="classic 16 bold")
txt.pack(expand=1,fill='both')

root.mainloop()
