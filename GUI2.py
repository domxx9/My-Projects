from tkinter import *

main=Tk()

ask_1 = Label(main, text="Please enter your flex:")
flex = Entry(main)
submit_flex = Button(main, "Submit")

ask_1.grid(row=0, column=0)
flex.grid(row=0, column=1)
submit_flex.grid(row=1, column=0)

main.mainloop()
