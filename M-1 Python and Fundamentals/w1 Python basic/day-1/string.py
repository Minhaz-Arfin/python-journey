#string in python are surronded by "" or ''. both are same
#ex: "this"/ 'this'

#QUOTES INSIDE A QUOTE
#you can use quotes inside a quotes as long as it 
#does not match surronded quotation

print("it's alright")
print("He is called 'Johny'")
print('She is called "Jessi"')

#assign a string to a variable
a = "hello"
print(a)

#MULTILINE STRING
#you can assign a multiple string to a variable by using three quotes

b= """loren ipsum hbfhf hbff bf f hwfbhfbgvfew wvf
    efbhf bfhf hbfewf"""
print(b)

#LOOPING THROUGH A STRING
#since strings are arrays, we can loop through the charecters in a string
#with a for loop

for c in "banana":
    print(c)
    
#STRING LENGTH
#To get the length of a string use len() function

d = "hello world"
print(len(d))

#CHECK STRING
#To check if a certain phase or charecter is present in an string use the keyword in()
txt = "sometime the best things in life are free!"
print("free" in txt) #true

#use it in if statement
txt = "sometime the best things in life are free!"
if "free" in txt:
    print(" YES! 'free' is present ")

#slicing
#you can return a range of charecters by using slice index
#specify start and end index, separated by a colon, to return part of the string

d = "hello world"
print(d[2:7]) #llo w

#SLICE from the start
#By leaving out the start index, the range will start at the first character:

d = "hello world"
print(d[:5]) #hello

#SLICE from the end
#By leaving out the end index, the range will go to the end:

print(d[6:]) #world

#NEG INDEXING
#Use negative indexes to start the slice from the end of the string:

print(d[-5:-2]) #wor

#UPPER CASE
#the upper() method converts lower case letters to upper case charecters

d = "hello world"
print(d.upper())

#LOWER CASE
#THE lower() method converts upper case letters to lower case
e = "HELLO WORLD"
print(e.lower())

#REMOVE WHITESPACE
#Whitespace is the space before and/or after the actual text, 
#and very often you want to remove this space , with strip()

d = " hello, world! "
print(d.strip()) #hello, world!

#REPLACE STRING
#The replace() method replaces a string with another string:

f = "hello world"
print(f.replace("l", "k")) #hekko workd

#SPLIT STRINGS
#The split() method returns a list where the text 
#between the specified separator becomes the list items.

d = "hello, world!"
print(d.split(",")) #['hello','world!']

#CONCATENATE STRING
#To concatenate, or combine, two strings you can use the + operator.

a= "hello"
b= "world"
c= a+" "+b
print(c) #hello world

#F- STRING
#To specify a string as an f-string, simply put an f in front of the string literal, 
# and add curly brackets {} as placeholders for variables and 
# other operations. Because string and int cannot be processed in same sentence.

age =35
txt = f"My name is Mahi, and I am {age}"
print(txt)

#ESCAPE CHARECTER
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#STRING METHODS
#Go to this link for details: https://www.w3schools.com/python/python_strings_methods.asp


