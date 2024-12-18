#FUNCTION
#a function is a block of code which only runs when it is called.
#you can pass data , known as parameters , into a function.
#a function cam return data as a result.

#CREATING A FUNCTION
#function is defined with def keyword:

def my_function():
    print("Hello, from a function")

#calling a function
my_function() #Hello, from a function

#ARGUMENTS
#information can be passed to functions using arguments
#Arguments are specified after the function name, inside the 
# parentheses. You can add as many arguments as you want, 
# just separate them with a comma.
def my_function(fname):
    print(fname+ " refsnes")
    
my_function("Emil")
#Arguments are often shortened to args in Python documentations.

#Parameters or Arguments?
#The terms parameter and argument can be used for the same thing: 
# information that are passed into a function.

#From a function's perspective:
#A parameter is the variable listed inside the parentheses 
# in the function definition.

#An argument is the value that is sent to the function 
# when it is called.

#NUMBER OF ARGUMENTS
#By default, a function must be called with the correct number of 
# arguments. Meaning that if your function expects 2 arguments, 
# you have to call the function with 2 arguments, not more, and not less.

def my_function(fname , lname):
    print(fname +" "+ lname) #Minhaz Arfin

my_function("Minhaz","Arfin") 

#ARBITRARY ARGUMENTS
#If you do not know how many arguments that will be passed into your 
# function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, 
# and can access the items accordingly:

def my_function(*kids):
    print("The youngest kid is "+ kids[2])  #The youngest kid is titir

my_function("anoli","tiara","titir")

#KEYWORD ARGUMENTS
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.

def my_function(child1,child2,child3):
    print("The eldest child is " + child1) #The eldest child is Anoli

my_function(child1="Anoli", child2="Tiara", child3="Titir")

#ARBITRARY KEYWORD ARGUMENTS , **kwargs
#If the number of keyword arguments is unknown, 
# add a double ** before the parameter name:

def my_function(**kid):
    print("her last name is "+ kid["lname"]) #her last name is Minhaz
    
my_function(fname="Anoli", lname= "Minhaz")

#DEFAULT PARAMETER VALUE
#If we call the function without argument, it uses the default value:

def my_function(country= "Bangladesh"):
    print("I am from " + country)

my_function()  #I am from Bangladesh

#PASSING A LIST AS AN ARGUMENT
#You can send any data types of argument to a function 
# (string, number, list, dictionary etc.), and it will 
# be treated as the same data type inside the function.
#if you send a List as an argument, 
# it will still be a List when it reaches the function:

def my_function(food):
    for x in food:
        print(x)

fruits = ["Apple","Banana", "cherry"]
my_function(fruits) #Apple #Banana #Cherry

#RETURN VALUES
#TO return function values use return function:

def my_function(x):
    return 5 * x

print(my_function(3))  #15
print(my_function(5)) #25
print(my_function(8))  #40

#THE PASS STATEMENT
#function definitions cannot be empty, but if you for some reason 
# have a function definition with no content, 
# put in the pass statement to avoid getting an error.

def my_function():
    pass

#POSITIONAL ONLY ARGUMENTS
#You can specify that a function can have ONLY positional arguments,
# or ONLY keyword arguments.
#To specify that a function can have only positional arguments, 
# add , / after the arguments:

def my_function(x, /):
  print(x)

my_function(3) #3

#kEYWORD ONLY ARGUMENTS
#To specify that a function can have only keyword arguments, 
# add *, before the arguments:

def my_function(*, x):
  print(x)

my_function(x = 8) #8


