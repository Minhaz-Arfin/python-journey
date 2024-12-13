#Write a program to check if a number is odd or even.

num = int(input("Enter a number: "))

if(num%2 ==0):
    print("The given number is an even number")
else:
    print("The given number is an odd number")

#Print the multiplication table of a given number.

mul = int(input("Enter a number: "))

for x in range(1,11):
    x = x*mul
    
    print(x)