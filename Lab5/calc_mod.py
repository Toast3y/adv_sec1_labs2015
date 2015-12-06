#Simple Calculator for Advanced Security 17

#Author: Christopher Jerrard-Dunne
#Student No: C12449618
#Date: 16/09/2015

#This simple calculator has simple functions and limited functionality, but can add, subtract, multiply and divide.

##import Tkinter to create a GUI
from Tkinter import *
from ttk import *
import Crypto.Util.number as RandGen
import tkMessageBox
import random

BLOCK_SIZE = 256
N = 10


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
	Label(root, justify="right", borderwidth="2", background="#00FF00", textvariable=screen_text).grid(row=0, columnspan=4)
	screen_text.set("0")

	#Add and pack Buttons
	Button(root, text="1", command = lambda: append_text(1)).grid(row=1, column=0)
	Button(root, text="2", command = lambda: append_text(2)).grid(row=1, column=1)
	Button(root, text="3", command = lambda: append_text(3)).grid(row=1, column=2)
	Button(root, text="4", command = lambda: append_text(4)).grid(row=2, column=0)
	Button(root, text="5", command = lambda: append_text(5)).grid(row=2, column=1)
	Button(root, text="6", command = lambda: append_text(6)).grid(row=2, column=2)
	Button(root, text="7", command = lambda: append_text(7)).grid(row=3, column=0)
	Button(root, text="8", command = lambda: append_text(8)).grid(row=3, column=1)
	Button(root, text="9", command = lambda: append_text(9)).grid(row=3, column=2)
	Button(root, text="0", command = lambda: append_text(0)).grid(row=4, column=0)
	Button(root, text="+", command = lambda: set_mode(0)).grid(row=2, column=3)
	Button(root, text="-", command = lambda: set_mode(1)).grid(row=3, column=3)
	Button(root, text="*", command = lambda: set_mode(2)).grid(row=4, column=2)
	Button(root, text="/", command = lambda: set_mode(3)).grid(row=4, column=3)
	Button(root, text="=", command = equals).grid(row=4, column=1)
	Button(root, text="Clear", command = clear_text).grid(row=1, column=3)
	Button(root, text="GenNum", command = generate_large_num).grid(row=5, column=0)
	Button(root, text="GenNum2", command = generate_large_num2).grid(row=5, column=1)
	Button(root, text="GenNPrimes", command = gen_n_primes).grid(row=5, column=2)
	Button(root, text="FindNext", command = generate_next_prime).grid(row=5, column=3)
	
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
	
def generate_large_num():
	#Generate a very large number for cryptographic purposes. Checks the number afterwards if it's prime or not. Recursively calls until it is prime.
	LargeNum = RandGen.getPrime(BLOCK_SIZE)
	if RandGen.isPrime(LargeNum) == True:
		tkMessageBox.showinfo("Large Number Generator", str(LargeNum) + " is a prime number.")
	else:
		generate_large_num()
	
def generate_large_num2():
	#Generate another large number using pythons in built random function. Checks if it's prime.
	LargeNum = random.getrandbits(BLOCK_SIZE)
	if RandGen.isPrime(LargeNum) == True:
		tkMessageBox.showinfo("Large Number Generator 2", str(LargeNum) + " is a prime number.")
	else:
		generate_large_num2()
		
def gen_n_primes():
	#Generate a list of 10 prime numbers
	global LargeNumList
	LargeNumList = []
	for x in range(0,N):
		LargeNum = RandGen.getPrime(BLOCK_SIZE)
		LargeNumList.append(LargeNum)
	tkMessageBox.showinfo("Large Number Generator List", str(LargeNumList))
	
	
def generate_next_prime():
	#Find a prime number, then find the next number in order
	PrimeNum = RandGen.getPrime(BLOCK_SIZE)
	PrimeNum2 = get_next_prime(PrimeNum + 2)
	tkMessageBox.showinfo("Next Prime Finder", str(PrimeNum) + " is a prime number, and " + str(PrimeNum2) + " is the next prime number after that.")
	
def get_next_prime(possible_prime):
	#Find the next number given a prime number, and return it
	if RandGen.isPrime(possible_prime) == True:
		return possible_prime
	else:
		possible_prime = get_next_prime(possible_prime + 2)
	return possible_prime

##Create layout object
root = Tk()

##Modify root window
root.title("Calculator")

##Initialize, Start main loop and render
initialize(root)
root.mainloop()