#there are three numeric types in python: int, float, complex
#variables of numeric types are created when you assign value to them
#ex: x = 1 (int); y= 2.8 (float); z= 1j (complex)
#To varify any types in python use this: print(type(x))

x = 5
y = 2.5
z = 35e3
e = 1j
print(type(x)) #int
print(type(y)) #float
print(type(z)) #float
print(type(e)) #complex

#TYPE CONVERSION
#convert one type to another
a= 1
b = 2.8
c =1j

#convert from int to float
r = float(a)
#convert from float to int
s = int(b)
#convert from int to complex
t = complex(c)
print(type(r)) #float
print(type(s)) #int
print(type(t)) #complex

#You Can not convert complex number to any other number type

#RANDOM NUMBER
#python doesnot have a random() function to create random numbers but
#python has a built in module called random that canbe used for creating random numbers

import random
print(random.randrange(1,10))

#more about random in python in https://www.w3schools.com/python/module_random.asp

