from tkinter import *



def doNothing():
    print("make me somethign usefull")

base = Tk()

menu = Menu(base)
base.config(menu=menu)

sub_menu = Menu(menu)
menu.add_cascade(label="About", menu=sub_menu)
sub_menu.add_command(label="About...", command=doNothing)
sub_menu.add_command(label="New...", command=doNothing)
sub_menu.add_separator()
sub_menu.add_command(label="Quit", command=doNothing)


"""
class dombutton:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.print_button = Button(frame, text = "Print Message", command=self.print_message)
        self.print_button.pack(side=LEFT)

        self.quit_button = Button(frame, text = "Quit", command=frame.quit)
        self.quit_button.pack(side=LEFT)

    def print_message(self):
        print("wow im doing it")

base = Tk()
d = dombutton(base)
"""
"""
def print_name(event):
    print("Hello im printing things")

button1 = Button(base,text="Button 1",)
button1.bind("<Button-1>", print_name)
button1.pack()
"""

""" entries and lables
lable_one =Label(base, text="First Name:")
lable_two =Label(base, text="Last Name:")

entry_one = Entry(base)
entry_two = Entry(base)

lable_one.grid(row=0, sticky=E)
entry_one.grid(row=0, column=1)
lable_two.grid(row=1, sticky=E)
entry_two.grid(row=1, column=1)

c = Checkbutton(base, text="Remember me")

c.grid(columnspan=2)

"""

""" layout
one = Label(base, text="One", bg="blue")
one.pack()
two = Label(base, text="Two", bg="green")
two.pack(fill=X)
three = Label(base, text="Three", bg="yellow")
three.pack(side=LEFT, fill=Y)
"""

""" button building
topframe = Frame(base)
topframe.pack(side=TOP)
bottomframe = Frame(base)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe,text="Button 1")
button2 = Button(topframe,text="Button 2")
button3 = Button(topframe,text="Button 3")
button4 = Button(bottomframe,text="Button 4")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
"""
base.mainloop()
