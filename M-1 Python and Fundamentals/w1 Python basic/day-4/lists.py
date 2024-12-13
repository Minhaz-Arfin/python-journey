#LISTS
#Lists are used to store multiple items in a single variable

thislist = ["Apple","banana", "cherry"]
print(thislist)

#List items are ordered, changeable, and allow duplicate values
#List items are indexed, the first item has index [0], the second item has index [1] etc.

#When we say that lists are ordered, it means that the items have a defined order, 
# and that order will not change.
#If you add new items to a list, the new items will be placed at 
# the end of the list.
#There are some list methods that will change the order, 
# but in general: the order of the items will not change.

#The list is changeable, meaning that we can change, add, and remove 
# items in a list after it has been created.
#Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#LIST LENGTH
#To determine how many items a list has, use the len() function:

thislist = ["Apple","banana", "cherry"]
print(len(thislist))

#LIST TYPE

mylist = ["Apple", "Banana", "Cherry"]
print(type(mylist)) #<class 'list'>

#THE LIST CONSTRUCTOR
#It is also possible to use the list() constructor when creating a new list.

#Using the list() constructor to make a List:
thislist = list(("apple","banana","cherry"))
print(thislist)

#ACCESS LIST
#List items are indexed and you can access them by referring to the index number:
thislist = ["Apple","banana", "cherry"]
print(thislist[1]) #banana

#NEGATIVE INDEXING
#Negative indexing means start from the end. -1 refers to the last item
#-2 refers to the second last item etc.

#print the last item of the list
thislist = ["Apple","banana", "cherry"]
print(thislist[-1]) #cherry

#RANGE OF INDEX
#Return the third, fourth and fifth item

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#RANGE OF NEGATIVE INDEXES
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']

#CHECK IF ITEM EXISTS
#to check if an item exits use in keyword
thislist = ["Apple","banana", "cherry"]
if "Apple" in thislist:
    print("Yes, Apple is on the list")

#CHANGE ITEM VALUE

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrent"
print(thislist)

#CHANGE THE RANGE OF ITEM VALUES
#To change the value of items within a specific range, 
# define a list with the new values, and refer to the 
# range of index numbers where you want to insert the new values:

thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3] = ["blackcurrent","watermelon"]
print(thislist)

#INSERT ITEMS
#to insert a list item, without replacing any of the existing values,
# we can use the insert() method. the method inserts an item at the specified index.

#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#ADD LIST ITEMS
#APPEND ITEMS
#To add an item to the end of the list, use the append() method:   
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#to add an item in a specific index use insert()

#EXTEND LIST
#TO append eliments from another list to current list, use extend()
thislist = ["apple", "banana", "cherry"]
topical = ["mango","pineapple","papaya"]

thislist.extend(topical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#ADD ANY ITERABLE
#The extend() method does not have to append lists, 
# you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistouple = ("kiwi", "orange")
thislist.extend(thistouple)
print(thislist) #['apple', 'banana', 'cherry', 'kiwi', 'orange']

#REMOVE SPECIFIED ITEMS
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple','cherry']

#If there are more than one item with the specified value,
# the remove() method removes the first occurrence:

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry', 'banana', 'kiwi']

#REMOVE SPECIFIED INDEX
# the pop() method removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #['apple', 'cherry']

#If you do not specify the index, the pop() method removes the last item.

#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #['banana', 'cherry']

#the del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

#CLEAR THE LIST
#the clear() method empties the list

print("Gap")

#LOOP THROUGH A LIST
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
 
print("gap")   
#LOOP THROUGH THE INDEX NUMBERS 

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#USING A WHILE LOOP
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#LIST COMPREHENSION
#List comprehension offers a shorter syntax when 
#you want to create a new list based on the values of an existing list.


#Based on a list of fruits, you want a new list, 
# containing only the fruits with the letter "a" in the name.

#Without list comprehension you will have to write a for statement 
# with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for  x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist) #['apple', 'banana', 'mango']

#but with list comprihension you can get this in a single line
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  #['apple', 'banana', 'mango']

#THE SYNTEX
#newlist = [expression for item in iterable if condition == True]

#CONDITION
# The condition works like filter
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"] #only accepts item that are not apple
print(newlist)

#accepts number only that are less than 5
newlist = [x for x in range(10) if x < 5]
print(newlist)

#SORT LIST ALPHANUMARICALLY
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) #[23, 50, 65, 82, 100]

#SORT DECENDING
#To sort descending, use the keyword argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#CUSTOMIZE SORT FUNCTION
#You can also customize your own function by using the keyword 
# argument key = function.
#The function will return a number 
# that will be used to sort the list (the lowest number first):

#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) #[50, 65, 23, 82, 100]

#By default the sort() method is case sensitive, resulting in 
#all capital letters being sorted before lower case letters:

#if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) #['banana', 'cherry', 'Kiwi', 'Orange']

#REVERSE ORDER
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #['cherry', 'Kiwi', 'Orange', 'banana']

#COPY LIST
#You cannot copy a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1, and 
# changes made in list1 will automatically also be made in list2.

#COPY METHOD**
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple","banana","cherry"]
mylist = thislist[:]
print(mylist)

#JOIN TWO LISTS
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3) #['a', 'b', 'c', 1, 2, 3]

#Another way to join two lists is by 
# appending all the items from list2 into list1, one by one:

list1 = ["a","b","c"]
list2 = [1,2,3]

for x in list2:
    list1.append(x)
    
print(list1) #['a', 'b', 'c', 1, 2, 3]

#Or you can use the extend() method, where the purpose is to 
# add elements from one list to another list:

list1 = ["a","b","c"]
list2 = [1,2,3]

list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]

#all list methods :https://www.w3schools.com/python/python_lists_methods.asp
