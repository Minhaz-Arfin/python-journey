#PYTHON CONDITIONALS & IF STATEMENT
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

a = 33
b =200

if(a<b):
    print("b is greater than a")
    
    #or
a = 33
b =200

if(a<b):
    txt =  f" {b} is greater than {a}"
    print(txt)

#ELIF
a=33
b=33

if(a>b):
    print("a is greater than b")
elif(a==b):
    print("a and b are equal")
    
#ELSE
a=33
b=200

if(a>b):
    print("a is greater than b")
elif(a==b):
    print("a and b are equal")
else:
    print("a is less than b")

#SHORT HAND IF
#If you have only one statement to execute, you can 
# put it on the same line as the if statement.

if a<b : print("a is less than b")

#SHORT HAND ELIF

a=2
b=330

print("A") if a>b else print("B")

#This technique is known as Ternary Operators, or Conditional Expressions.
#You can also have multiple else statements on the same line:

a=330
b=330
print("A") if a>b else print("B") if a<b else print("=")

#AND
#the and keyword is a logical operator, and is used to combine conditional statements

#test if a is greater than b and c is greater than a
a=33
b=20
c=50

if a>b and c>a:
    print("both conditions are true")

#OR
#test if a is greater than b or a is greater than c

a=33
b=20
c=50

if a>b or a>c:
    print("At least one of the conditions are true")

#NOT
#test if a is not greater than b

a=33
b=200

if not a>b:
    print("a is not greater than b")
    
#NESTED IF
#You can have if statements inside if statements, this is called nested if statements.

x =18

if(x>10):
    print("x is above 10")
    if(x>20):
        print("And also above 20")
    else:
        print("But not above 20")

#THE PASS STATEMENT
#if statements cannot be empty, but if you for some reason have an if statement 
# with no content, put in the pass statement to avoid getting an error.

a,b =33, 200
if(a<b):
    pass

