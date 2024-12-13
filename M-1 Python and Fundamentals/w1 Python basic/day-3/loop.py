#WHILE LOOPS
#With the while loop we can execute a set of statements as long as a condition is true.

#Print i as long as i is less than 6:
i=1
while i<6:
    print(i)
    i=i+1

#THE BREAK STATEMENT
#With the break statement we can stop the loop even if the while condition is true:
print("gap")
#Exit the loop when i is 3:
i=1
while i<7:
    print(i)
    if(i==3):
        break
    i=i+1

#THE CONTINUE STATEMENT
#With the continue statement we can stop the current iteration, 
# and continue with the next:
print("gap")
#continue to the next iteration if i=3
i=0
while i<6:
    i=i+1
    if(i==3):
        continue
    print(i)
    
#THE ELSE STATEMENT
#With the else statement we can run a block of code 
# once when the condition no longer is true:

#Print a message once the condition is false:
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i no longer less than 6")
    
#FOR LOOPS
fruits = ["apple","banana", "cherry"]
for x in fruits:
    print(x)

#LOOPING THROUGH A STRING
#Even strings are iterable objects, they contain a sequence of characters:

for x in "banana":
    print(x)

#THE BREAK STATEMENT
#With the break statement we can stop the loop 
# before it has looped through all the items:

#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break #apple, banana

#2
fruits = ["apple","banana","cherry"]
for x in fruits:
    if(x=="banana"):
        break
    print(x) #apple

print("gap")
    
#THE CONTINUE STATEMENT
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
#THE RANGE FUNCTION
#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 (by default), and 
# ends at a specified number.

for x in range(6):
    print(x)

for x in range (2,6):
    print(x)
print("gap")  
for x in range(2, 30, 3): #from 2 to 30 with the gap of 3
  print(x) #2,5,8,11,14,17,20,23,26,29

#ELSE IN FOR LOOP

for x in range(6):
    print(x)
else:
    print("finally finished")

#The else block will NOT be executed if the loop is 
# stopped by a break statement.

#Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
    if x==3: break
    print(x)
else:
    print("finally finished")
    
#NESTED FOR LOOPS

adj = ["red","big","tasty"]
fruits=["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)