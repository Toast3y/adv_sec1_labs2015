#Simple Calculator for Advanced Security 17

#Author: Christopher Jerrard-Dunne
#Student No: C12449618
#Date: 16/09/2015

#This simple calculator has simple functions and limited functionality, but can add, subtract, multiply and divide.

##import Tkinter to create a GUI
from Tkinter import *
from ttk import *


##Define functions for use in application
def initialize(root):
	#create "screen" label and variable to display results
	#Declare and initialize all global variables
	global screen_text, working_number, number1, number2, mode
	screen_text = StringVar()
	working_number = ""
	mode = -1
	number1 = 0
	number2 = 0
	screen = Label(root, justify="right", borderwidth="2", background="#00FF00", textvariable=screen_text).grid(row=0)
	screen_text.set("0")

	#Add and pack Buttons
	button_1 = Button(root, text="1", command = lambda: append_text(1)).grid(row=1, column=0)
	button_2 = Button(root, text="2", command = lambda: append_text(2)).grid(row=1, column=1)
	button_3 = Button(root, text="3", command = lambda: append_text(3)).grid(row=1, column=2)
	button_4 = Button(root, text="4", command = lambda: append_text(4)).grid(row=2, column=0)
	button_5 = Button(root, text="5", command = lambda: append_text(5)).grid(row=2, column=1)
	button_6 = Button(root, text="6", command = lambda: append_text(6)).grid(row=2, column=2)
	button_7 = Button(root, text="7", command = lambda: append_text(7)).grid(row=3, column=0)
	button_8 = Button(root, text="8", command = lambda: append_text(8)).grid(row=3, column=1)
	button_9 = Button(root, text="9", command = lambda: append_text(9)).grid(row=3, column=2)
	button_0 = Button(root, text="0", command = lambda: append_text(0)).grid(row=4, column=0)
	button_plus = Button(root, text="+", command = lambda: set_mode(0)).grid(row=2, column=3)
	button_minus = Button(root, text="-", command = lambda: set_mode(1)).grid(row=3, column=3)
	button_multiply = Button(root, text="*", command = lambda: set_mode(2)).grid(row=4, column=2)
	button_divide = Button(root, text="/", command = lambda: set_mode(3)).grid(row=4, column=3)
	button_equals = Button(root, text="=", command = equals).grid(row=4, column=1)
	button_clear = Button(root, text="Clear", command = clear_text).grid(row=1, column=3)
	
def set_mode(setmode):
	#Set the mode of the calculator function and store the first number
	global working_number, number1, screen_text, mode
	
	#Edge case: If you require minus numbers
	if setmode == 1 and working_number == "":
		working_number = "-"
		screen_text.set(working_number)
	else:
		number1 = int(working_number)
		mode = setmode
		working_number = ""

def equals():
	#Use the mode to calculate the answer
	global working_number, number1, number2, mode, screen_text
	number2 = int(working_number)
	working_number = ""
	
	if mode == 0:
		screen_text.set(number1+number2)
	elif mode == 1:
		screen_text.set(number1-number2)
	elif mode == 2:
		screen_text.set(number1*number2)
	elif mode == 3:
		if number1 == 0 or number2 == 0:
			screen_text.set ("You cannot divide by zero.")
		else:
			screen_text.set (number1/number2)
	
	number1 = 0
	number2 = 0
	
def append_text(number):
	#Handle numbers and update screen similar to a real world calculator people expect
	global screen_text, working_number
	working_number = (working_number + str(number))
	screen_text.set(working_number)
	
def clear_text():
	#Clear all working variables, "zeroes" the calculator
	global screen_text, working_number, number1, number2, mode
	mode = -1
	working_number = ""
	number1 = 0
	number2 = 0
	screen_text.set("0")

##Create layout object
root = Tk()

##Modify root window
root.title("Calculator")

##Initialize, Start main loop and render
initialize(root)
root.mainloop()