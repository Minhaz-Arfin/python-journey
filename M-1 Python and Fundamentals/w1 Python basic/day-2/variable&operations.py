#VARIABLES
#Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.

#CASTING
#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#variable names are case sensitive

#MANY VALUES TO MULTIPLE VARIABLE
#Python allows you to assign values to multiple 
# variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#ONE VALUE TO MULTIPLE VARIABLES
#Also you can assign just one value to multiple variables
x = y = z = "orange"
print(x)
print(y)
print(z)

#UNPACK A COLLECTION
#If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. 
# This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #python is awesome
# you can also use the + operator to output multiple variables

#GLOBAL VARIABLES
# variables that are created outside of the function are known as 
# global variables. global variables can be used by everyone, 
# both inside and outside of the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#THE GLOBAL KEYWORD
#When you create a variable inside a function, that variable is local
#and can only be used inside that function.
#To create a global variable inside a function, you can use a global keyword

def myfunc():
    global x
    x= "fantastic"
    
myfunc()
print("python is ", x) #python is fantastic

#PYTHON OPERATORS : https://www.w3schools.com/python/python_operators.asp

#STRING MANIPULATIONS: https://www.w3schools.com/python/python_ref_string.asp



