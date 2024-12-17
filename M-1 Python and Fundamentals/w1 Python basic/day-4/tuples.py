#TUPLES
#Tuples are used to store multiple items in a single variable.

#CRETING A TUPLE
thistuple = ("apple","banana","cherry")
print(thistuple)

#Tuple items are ordered, unchangeable, and allow duplicate values.
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

#tuples allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#tuple length
print(len(thistuple)) #5

#CREATE TOUPLE WITH ONE ITEM
#To create a tuple with only one item, you have to add a comma 
# after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple)) #<class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #<class 'str'>

#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

#THE TUPLE CONSTRUCTOR
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#ACCESS TUPLE
thistuple = ("apple","banana","cherry")
print(thistuple[1]) #banana

#negative indexing
thistuple = ("apple","banana","cherry")
print(thistuple[-1]) #cherry

#range of indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #('cherry', 'orange', 'kiwi')

#UPDATE TUPLES
#Tuples are unchangeable, meaning that you cannot change, add, or 
# remove items once the tuple is created. But there are some workarounds.

#CHANGE TUPLE VALUES
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, 
# change the list, and convert the list back into a tuple.

#Convert the tuple into a list to be able to change it:
x = ("apple","banana","cherry")
y = list(x) #list constructor
y[1] = "kiwi"
x = tuple(y) #tuple constructor

print(x) #('apple', 'kiwi', 'cherry')

#ADD ITEMS TO TUPLE
#since tuples are immutable, there is no append() function built in for tuple
#but you can add with some modification to add items un tuple

#1.Convert into a list
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

#2. ADD tuple to tuple
thistuple = ("apple","banana","cherry")
y = ("orange",)
thistuple += y
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

#NOte: When creating a tuple with only one item, remember to include 
# a comma after the item, otherwise it will not be identified as a tuple.

#REMOVE ITEM
#SINCE Tuples are unchangeable, there is no direct way to delete items

thistuple = ("apple","banana","cherry")
y = list(thistuple) #convert it to a list
y.remove("apple")
thistuple = tuple(y) #convert back to tuple
print(thistuple) #('banana', 'cherry')

#TO DEL the tuple completely
thistuple = ("apple","banana","cherry")
del thistuple

#UNPACKING TUPLE
#When we create a tuple, we normally assign values to it. 
# This is called "packing" a tuple:

#Packing a tuple:
fruits = ("apple","banana","cherry")

#But, in Python, we are also allowed to extract 
# the values back into variables. This is called "unpacking":
fruits = ("apple","banana","cherry")
(green,yellow,red) = fruits
print(green) #apple
print(yellow) #banana
print(red) #cherry

#Note: The number of variables must match the number of values in the 
# tuple, if not, you must use an asterisk to 
# collect the remaining values as a list.

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
#Assign the rest of the values as a list called "red":
print(green)
print(yellow)
print(red) #apple banana ['cherry', 'strawberry', 'raspberry']

#If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number 
# of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red) #apple
            #['mango', 'papaya', 'pineapple']
            #cherry

#LOOP THROUGH THE TUPLE WITH INDEX NUMBER
thistuple =("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i]) #apple banana cherry
    
#JOIN TWO TUPLES
#join two tuples by using the "+" operator

x = ["a","b","c"]
y = ["d","e","f"]
tuple1 = x+y
print(tuple1) #['a', 'b', 'c', 'd', 'e', 'f']

#MULTIPLY TUPLES
#If you want to multiply the content of a tuple a given number of 
# times , you can use the * operator:

#Multiply the fruits tuple by 2:
fruits =( "apple","banana","cherry")
mytuple = fruits * 2
print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

#TUPLE METHODS
#https://www.w3schools.com/python/python_tuples_methods.asp


