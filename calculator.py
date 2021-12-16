from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0,column=0, columnspan=3,)

def button_click(num):
	current = e.get()
	e.delete(0, END)
	e.insert(0,str(current) + str(num))

def button_clear():
	e.delete(0, END)


def button_add():
    first_number = e.get()
    global first_num
    first_num = int(first_number)
    e.delete(0,END)

def button_equal():
	second_number = e.get()
	second_num = int(second_number)
	e.delete(0,END)
	total = first_num + second_num
	e.insert(0,total)

	
myButton = Button(root, text = "1", width=10 ,height=3, command=lambda: button_click(1)).grid(row=1,column=0,padx=3,pady=3)
myButton1 = Button(root, text = "2", width=10 ,height=3, command=lambda: button_click(2)).grid(row=1,column=1,padx=3,pady=3)
myButton2 = Button(root, text = "3", width=10 ,height=3, command=lambda: button_click(3)).grid(row=1,column=2,padx=3,pady=3)
myButton3 = Button(root, text = "4", width=10 ,height=3, command=lambda: button_click(4)).grid(row=2,column=0,padx=3,pady=3)
myButton4 = Button(root, text = "5", width=10 ,height=3, command=lambda: button_click(5)).grid(row=2,column=1,padx=3,pady=3)
myButton5 = Button(root, text = "6", width=10 ,height=3, command=lambda: button_click(6)).grid(row=2,column=2,padx=3,pady=3)
myButton6 = Button(root, text = "7", width=10 ,height=3, command=lambda: button_click(7)).grid(row=3,column=0,padx=3,pady=3)
myButton7= Button(root, text = "8", width=10 ,height=3, command=lambda: button_click(8)).grid(row=3,column=1,padx=3,pady=3)
myButton8 = Button(root, text = "9", width=10 ,height=3, command=lambda: button_click(9)).grid(row=3,column=2,padx=3,pady=3)
myButton0 = Button(root, text = "0", width=10 ,height=3, command=lambda: button_click(0)).grid(row=4,column=0,padx=3,pady=3)
clearButton = Button(root, text = "Clear", width=23 ,height=3, command=button_clear).grid(row=4,column=1,padx=3,pady=3,columnspan=2)
plusButton = Button(root, text = "+", width=10 ,height=3, command=button_add).grid(row=5,column=0,padx=3,pady=3)
equalButton = Button(root, text = "=", width=23 ,height=3, command=button_equal).grid(row=5,column=1,padx=3,pady=3,columnspan=2)
root.mainloop()
