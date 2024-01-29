#Programmer: Dylan
#Program: Variables and Methods
#Date: 1.11.2024

quote = "its everyday bro."
print(quote)

print(quote.upper()) #Uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #length of the characters in the quote
name = "Dylan" #string
age = 33 #int
gpa = 4.2 #float - has a decimal
print(age)
print(int(gpa)) #cast a float into a int

print("\nMy name is " + name + " and i am " + str(age) + " with a GPA of " + str(gpa) + ".") # concatenate variables while casting int to str


print("\nMy name is ",name," and i am ",age," with a GPA of "+ str(gpa) + ".") #Connecting using a coma instead of awhile casting our GPA variable into a string to account for the spacing before the period

print("")

age += 1 #adds 1 to the variable age
print(age)

print("")

age += 10#adds 10 to the variable age
print(age)

print("")

birthday = 1
age += birthday #We can add two variables with the values as intagers together
print(age)
