from Tkinter import *
from  tkFileDialog import *

filename = None

def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0,END)

def saveFile():
	global filename
	t = text.get(0.0, END)
	f = open(filename, 'w')
	f.write(t)
	f.close()

def saveAs():
	f = asksaveasfile(mode='w',defaultextension = '.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title="Oops!",message = "Cant be saved :(")

def openFile():
	f = askopenfile(mode = 'r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)





root = Tk()
root.title("My Editor")
root.minsize(width = 400, height = 400)
root.maxsize(width = 400, height = 400)

text = Text(root, width=400, height = 400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New" , command=newFile)
filemenu.add_command(label="Open" , command=openFile)
filemenu.add_command(label="Save" , command=saveFile)
filemenu.add_command(label="SaveAs.." , command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit" , command=root.quit)
menubar.add_cascade(label = "File", menu = filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label="Cut",command = cut)
editmenu.add_command(label="Copy",command = Copy)
editmenu.add_command(label="Paste",command = Paste)
menubar.add_cascade(label = "Edit" ,menu = editmenu)

root.config(menu = menubar)
root.mainloop()
