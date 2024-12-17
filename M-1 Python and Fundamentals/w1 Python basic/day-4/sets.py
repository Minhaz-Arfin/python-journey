#Sets are used to store multiple items in a single variable.
#Set items are unchangeable, but you can remove items and add new items.

#CREATE A SET
thisset = {"apple","banana","cherry"}
print(thisset)       #{'cherry', 'banana', 'apple'}

#Note: Sets are unordered, so you cannot be sure in which order 
# the items will appear.

#Set items are unordered, unchangeable, 
# and do not allow duplicate values.
#Set items can appear in a different order every time you use them, 
# and cannot be referred to by index or key.

#Set items are unchangeable, meaning that we cannot change the items 
# after the set has been created

#Duplicate values in a set will be ignored.
thisset = {"apple","banana","apple","cherry","Banana"}
print(thisset)      #{'cherry', 'banana', 'Banana', 'apple'}

#set is case sensitive ,thats why it took banana and Banana 
#but ignored apple the second time

#Note: The values True and 1 are considered the same value in sets, 
# and are treated as duplicates:

#The values False and 0 are considered the same value in sets, 
# and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2, False, 3 , 0}
print(thisset)       #{False, True, 2, 3, 'cherry', 'apple', 'banana'}

#length of a set
thisset = {"apple","banana","cherry"}
print(len(thisset))     #3

#A set can contain different data types:
#A set with different types of data -->

set1 = {"abc", 34, True, 40, "male"}

#TYPE SET
myset = {"apple", "banana", "cherry"}
print(type(myset))  #<class 'set'>

#THE SET CONSTRUCTOR
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#ACCESS ITEMS IN SET
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, or ask if a
# specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)   #cherry banana apple
    

#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)      #True

#Check if "banana" is not present in the set:
thisset = {"apple","banana", "cherry"}
print("banana" not in thisset)  #False

#Once a set is created, you cannot change its items, but you can add new items.

#ADD ITEMS
#to add one item to a set use add()
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)      #{'orange', 'apple', 'cherry', 'banana'}

#ADD SETS
#TO Add items of another set to a set use update() method

thisset = {"apple", "banana", "cherry"}
topical = {"pineapple","mango", "papaya"}

thisset.update(topical)
print(thisset)  #{'cherry', 'pineapple', 'mango', 'banana', 'papaya', 'apple'}

#The object in the update() method does not have to be a set, it 
# can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
topical = ["pineapple","mango", "papaya"]
thisset.update(topical) 
print(thisset) #{'cherry', 'pineapple', 'mango', 'banana', 'papaya', 'apple'}

#REMOVE
#to remove any item in a set use remove() or discard() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)  #{'banana', 'cherry'}

thisset = {"apple", "banana", "cherry"}
thisset.discard("cherry")
print(thisset) #{'apple', 'banana'}

#Note: If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop() method to remove an item, 
# but this method will remove a random item, 
# so you cannot be sure what item that gets removed
#the return value of pop() method is the removed item


#The clear() method empties the set:
thisset = {"apple","banana","cherry"}
thisset.clear()
print(thisset) #set()

#the del keyword will delete the set completely
thisset = {"apple","banana","cherry"}
del thisset

#LOOP SETS
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(thisset) #{'apple', 'banana', 'cherry'}

#JOIN SETS IN PYTHON

#1. UNION METHOD:
# the union method returns a new set with all items from both sets.

set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)  #{1, 'a', 2, 3, 'c', 'b'}

#You can use the | operator instead of the union() method, 
# and you will get the same result.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) #{'b', 'c', 1, 2, 3, 'a'}

#join multiple sets with union / "|"
set1 = {"a", "b"}
set2 = {1, 3}
set3 = {"John", "cina"}
set4 = {"pineapple","mango"}

set5 = set1 | set2 | set3 | set4
print(set5)  #{1, 'John', 3, 'b', 'a', 'mango', 'pineapple', 'cina'}

#JOIN A SET WITH TUPLES
#THE union method allows to join a set with any other types like tuple
set1 = {"a", "b"}
tuple1 = (1,3)

set3 = set1.union(tuple1)
print(set3)  #{'b', 'a', 3, 1}

#Note: The  | operator only allows you to join sets with sets, 
# and not with other data types like you can with the  union() method.

#UPDATE
#The update() method inserts all items from one set into another.
#The update() changes the original set, and does not return a new set.

set1 = {"a", "b"}
set2 = {1, 3}
set1.update(set2)
print(set1) #{'a', 3, 'b', 1}

#2. INTERSECTION METHOD
# This method will only keep the duplicate values from both sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) #{'apple'}

#You can use the & operator instead of the intersection() method, 
# and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) #{'apple'}

#The & operator only allows you to join sets with sets, and not with 
# other data types like you can with the intersection() method.

#3.DIFFERENCE
#The difference() method will return a new set that will contain ONLY
# the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3) #:{'banana', 'cherry'}

#You can use the - operator instead of the difference() method, 
# and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) #:{'banana', 'cherry'}

#Note: The - operator only allows you to join sets with sets, and not 
# with other data types like you can with the difference() method.

#The difference_update() method will also keep the items from the 
# first set that are not in the other set, but it will 
# change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1) #{'cherry', 'banana'}


#4. THE SYMMETRIC DIFFERENCE()
#The symmetric_difference() method will keep only the elements that 
# are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) #{'google', 'cherry', 'microsoft', 'banana'}

#You can use the ^ operator instead of the symmetric_difference() method, 
# and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3) #{'google', 'cherry', 'microsoft', 'banana'}

#The ^ operator only allows you to join sets with sets, and not with 
#other data types like you can with the symmetric_difference() method.

#The symmetric_difference_update() method will also keep all but the 
# duplicates, but it will change the original set instead of 
# returning a new set.

#set methods: https://www.w3schools.com/python/python_sets_methods.asp



