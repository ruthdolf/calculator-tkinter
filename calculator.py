from tkinter import *
root = Tk()
root.title("Calculator")

e = Entry(root, width=30, borderwidth=4)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(number):
    current = e.get() #fetches the current content in entry box
    e.delete(0, END) #deletes everything in entry box (from char index 0 to the last)
    e.insert(0, str(current)+str(number)) #show the new input
    
def add(): #doesn't perform addition
    firstnum = e.get() #fetches the current content in entry box
    global fnum #global -> equal() can access this variable
    global math
    math = "addition"
    fnum = int(firstnum)
    e.delete(0, END)
    
def subtract():
    firstnum = e.get()
    global fnum
    global math
    math = "subtraction"
    fnum = int(firstnum)
    e.delete(0, END)

def multiply():
    firstnum = e.get()
    global fnum
    global math
    math = "multiplication"
    fnum = int(firstnum)
    e.delete(0, END)

def divide():
    firstnum = e.get()
    global fnum
    global math
    math = "division"
    fnum = int(firstnum)
    e.delete(0, END)
    
def clear():
    e.delete(0, END)
    
    
def equal(): #performs arithmetic operations
    secondnum = e.get()
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, fnum + int(secondnum)) #show sum in entry box

    if math == "subtraction":
        e.insert(0, fnum - int(secondnum))
        
    if math == "multiplication":
        e.insert(0, fnum * int(secondnum))       
        
    if math == "division":
        e.insert(0, fnum / int(secondnum))
    
    
#Define buttons
button1 = Button(root, text="1", width=5, pady=20, command=lambda: click(1))
button2 = Button(root, text="2", width=5, pady=20, command=lambda: click(2))
button3 = Button(root, text="3", width=5, pady=20, command=lambda: click(3))
button4 = Button(root, text="4", width=5, pady=20, command=lambda: click(4))
button5 = Button(root, text="5", width=5, pady=20, command=lambda: click(5))
button6 = Button(root, text="6", width=5, pady=20, command=lambda: click(6))
button7 = Button(root, text="7", width=5, pady=20, command=lambda: click(7))
button8 = Button(root, text="8", width=5, pady=20, command=lambda: click(8))
button9 = Button(root, text="9", width=5, pady=20, command=lambda: click(9))
button0 = Button(root, text="0", width=5, pady=20, command=lambda: click(0))

button_add = Button(root, text="+", width=5, pady=20, command=add)
button_subtract = Button(root, text="-", width=5, pady=20, command=subtract)
button_multiply = Button(root, text="x", width=5, pady=20, command=multiply)
button_divide = Button(root, text="÷", width=5, pady=20, command=divide)

button_equal = Button(root, text="=", width=5, pady=20, command=equal)
button_clear = Button(root, text="Clear", width=5, pady=20, command=clear)

#empty space
empty1 = Label(root, text="").grid(row=5, column=0, sticky="nsew")
empty2 = Label(root, text="").grid(row=5, column=2, sticky="nsew")


#put buttons on the screen
button1.grid(row=4, column=0, sticky="nsew")
button2.grid(row=4, column=1, sticky="nsew")
button3.grid(row=4, column=2, sticky="nsew")

button4.grid(row=3, column=0, sticky="nsew")
button5.grid(row=3, column=1, sticky="nsew")
button6.grid(row=3, column=2, sticky="nsew")

button7.grid(row=2, column=0, sticky="nsew")
button8.grid(row=2, column=1, sticky="nsew")
button9.grid(row=2, column=2, sticky="nsew")

button0.grid(row=5, column=1, sticky="nsew")

button_add.grid(row=4, column=3, sticky="nsew")
button_subtract.grid(row=3, column=3, sticky="nsew")
button_multiply.grid(row=2, column=3, sticky="nsew")
button_divide.grid(row=1, column=3, sticky="nsew")


button_clear.grid(row=1, column=0, sticky="nsew")
button_equal.grid(row=5, column=3, sticky="nsew")


root.mainloop()