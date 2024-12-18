#PYTHON SCOPE
#A variable is only available from inside it's region it is created.
#this is called scope

#LOCAL SCOPE
#A variable created inside a function belongs to the local scope 
# of that function, and can only be used inside that function.

#A variable created inside a function is available inside that function:
def myfunc():
    x=200
    print(x)

myfunc() #200

#FUNCTION INSIDE A FUNCTION
#As explained in the example above, the variable x is not available 
# outside the function, 
# but it is available for any function inside the function:

#The local variable can be accessed from a function within the function
def myfunc():
    x = 230
    def my_newf():
        print(x)
    my_newf()

myfunc() #230

#GLOBAL SCOPE
#A variable created in the main body of the Python code is a global 
# variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.
#A variable created outside of a function is global and can be used by anyone:

x=300
def myfunc():
    print(x)
myfunc()    #300
print(x)    #300

#NAMING VARIABLES
#If you operate with the same variable name inside and outside of a 
# function, Python will treat them as two separate variables, 
# one available in the global scope (outside the function) and 
# one available in the local scope (inside the function):

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()  #200

print(x)    #300

#GLOBAL KEYWORD
#If you need to create a global variable, but are stuck in the local 
# scope, you can use the global keyword.
#The global keyword makes the variable global.

#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x=450
myfunc()


print(x) #450

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x) #200

#NonLocal keyword
#The nonlocal keyword is used to work with variables inside nested functions.
#If you use the nonlocal keyword, the variable will belong to the outer function:

def myfunc():
    x = "jane"
    def myfunc2():
        nonlocal x
        x= "Ben"
    myfunc2()
    return x
print(myfunc())  #Ben
