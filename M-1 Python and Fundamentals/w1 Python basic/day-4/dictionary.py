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
  
