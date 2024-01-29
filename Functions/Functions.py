#Programmer: Dylan Bellinger
#Program: Functions
#Date: 1.19.2024 

def nl():#new line function
	print("\n")

def who_am_i(): #this is a functions without parameters
	name = "Himmy" # local variable
	age = 15
	print("my name is",name,"and I am",age,"years old.")

who_am_i()

nl()

def AddOneHundred(num): #num is a parameter
	print(num + 100)
	
AddOneHundred(1500) # 1500 is the argument which inserts itself into the the parameter
 
nl()

AddOneHundred(0)

nl()

def add(x,y):
	print(x + y)
	
add(8,4)

nl()

