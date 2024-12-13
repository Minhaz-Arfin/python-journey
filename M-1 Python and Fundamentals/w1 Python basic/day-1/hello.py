print("Hello, World!")

#PYTHON INDENTATION
#python uses indentation to indicate a 
#block of code.

if (5>2):
    print("5 is greater than 2")
#python will give error if indentation is missed

#DATA TYPES
#text : str
#numeric: int, float, complex
#sequence: list, tuple, range
#mapping: dict
#set type: set, frozenset
#boolean: bool
#binary: bytes, bytearray, memoryview
#none type: NoneType
x = 5
y = "red"
print(type(x))
print(type(y))

#if you want to specify data types:
z = float(3.14)
print(type(z))

t = list(("apple", "banana", "mango"))
print(t)

m = tuple (("orange", "date", "lemon"))
print(m)

n = range(6)
print(n)

#TAKE INPUT FROM USER
#Python 3.6 uses the input() method.

username = input("Enter username:")
print("Username is: " + username)