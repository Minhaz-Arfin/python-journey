thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and 
# do not allow duplicates.

#Dictionaries are written with curly brackets, and have keys and values:

#DICTIONARY ITEMS
#Dictionary items are ordered, changeable, and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be 
# referred to by using the key name.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(thisdict["model"]) #Mustang

#Dictionaries cannot have two items with the same key:

#DICTIONARY LENGTH
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(len(thisdict)) #3

#The values in dictionary items can be of any data type:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964,
    "colors": ["red","black","blue"]
}
print(type(thisdict))   #<class 'dict'>

#THE DICTIONARY CONSTRUCTOR
thisdict = dict(name="john",age = 35, country="Australia")
print(thisdict) #{'name': 'john', 'age': 35, 'country': 'Australia'}

#ACCESSING THE DICTIONARY ITEMS
#You can access the items of a dictionary by referring to 
# its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x= thisdict["model"]
print(x) #Mustang

#there is also a method called get(), that will give you the same result
x = thisdict.get("year")
print(x) #1964

#GET KEYS
#the keys() method will give you all the key list in the dict.
x = thisdict.keys()
print(x)  #dict_keys(['brand', 'model', 'year'])

#The list of the keys is a view of the dictionary, meaning that any 
# changes done to the dictionary will be reflected in the keys list.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x= car.keys()
print(x) #before the change--> dict_keys(['brand', 'model', 'year'])

car["color"] = "white"
print(x) #after the change --> dict_keys(['brand', 'model', 'year', 'color'])

#GET VALUES
#THE values() method will return a list of all the values in the dict.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x) #dict_values(['Ford', 'Mustang', 1964])

#GET ITEMS
#The items() method will return each item in a dictionary, 
# as tuples in a list.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
X= thisdict.items()
print(x)  #dict_values(['Ford', 'Mustang', 1964])

#CHECK IF KEY EXITS
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
#CHANGE VALUES
#you can change values of a specific item by reffering to its key name:

thisdict = {
  "brand" : "Ford",
  "model" : "Mustang",
  "year" : 1964
}
thisdict["year"]= 2018
print(thisdict)
  
#UPDATE DICTIONAY
#update() method will update the dictionary with items from the given arguments
#the argument must be a dictionary or an iterable object with key:value pairs

#Update the "year" of the car by using the update() method:
thisdict = {
  "brand" : "Ford",
  "model" : "Mustang",
  "year" : 1964
}
thisdict.update({"year":2020})
print(thisdict)

#ADDING ITEMS
#adding items is done by using a new index key and assigning a value to it

thisdict = {
  "brand" : "Ford",
  "model" : "Mustang",
  "year" : 1964
}
thisdict["colors"] = "red"
print(thisdict)

#REMOVE DICTIONARY ITEMS

#POP() method removes the item with specified key name 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)  #{'brand': 'Ford', 'year': 1964}

#POPITEMS()
#The popitem() method removes the last inserted item 
# (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang'}

#DEL
#the del() keyword removes item with specific key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) #{'brand': 'Ford', 'year': 1964}

#the del keyword can also delete the dictionary entirely

#CLEAR()
#the clear() method empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()



# LOOP THROUGH A DICTIONAY
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#you can loop through a dictionary using a for loop
#When looping through a dictionary, the return value are the keys 
#of the dictionary, but there are methods to return the values as well.

#Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

#print all the values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x])

#You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

#you can also use the keys() method to return keys of a dictionary:
for x in thisdict.keys():
  print(x)

#Loop through both keys and values, by using items method:
for x,y in thisdict.items():
  print(x)
  
#COPY DICTIONARY:

#You cannot copy a dictionary simply by typing dict2 = dict1, 
# because: dict2 will only be a reference to dict1, 
# and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the 
# built-in Dictionary method copy()

#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year" :1964
}
mydict = thisdict.copy()
print(mydict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#NESTED DICTIONARY
#a dictionay can contain dictionaries, this is called nested dictionaries

myfamily = {
  "child1": {
    "name" : "Anoli",
    "year" : 2018
  },
  "child2" : {
    "name" : "Tiara",
    "year" : 2020
  },
  "child3" : {
    "name" : "Titir",
    "year" : 2022
  }
}
print(myfamily) #{'child1': {'name': 'Anoli', 'year': 2018}, 'child2': {'name': 'Tiara', 'year': 2020}, 'child3': {'name': 'Titir', 'year': 2022}}

# OR you can add three dictionaries into one dictionary by following:
child1= {
    "name" : "Anoli",
    "year" : 2018
  }
child2 = {
    "name" : "Tiara",
    "year" : 2020
  }
child3 = {
    "name" : "Titir",
    "year" : 2022
  }

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(myfamily)

#ACCESS ITEMS IN NESTED DICTIONARY:
#To access items from a nested dictionary, you use the name of the 
# dictionaries, starting with the outer dictionary:

print(myfamily["child1"]["name"])  #Anoli

#LOOP THROUGH A NESTED DICTIONARY
#You can loop through a dictionary by using the items() method like this:

#Loop through the keys and values of all nested dictionaries:
for x,obj in myfamily.items():
  print(x)
  
  for y in obj:
    print(y + ':' ,obj[y])  #child1
                            #name: Anoli
                            #year: 2018
                            #child2
                            #name: Tiara
                            #year: 2020
                            #child3
                            #name: Titir
                            #year: 2022

#dictionary methods: https://www.w3schools.com/python/python_dictionaries_methods.asp
