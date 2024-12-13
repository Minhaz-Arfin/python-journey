#Swap two numbers without using a temporary variable.
#Check if a given string is a palindrome.

# Taking input for the two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Before swapping:")
print("num1 =", num1)
print("num2 =", num2)

# Swapping without using a temporary variable
num1, num2 = num2, num1

print("After swapping:")
print("num1 =", num1)
print("num2 =", num2)


# Taking input for the string
input_string = input("Enter a string: ")

# Removing spaces and converting to lowercase for a case-insensitive check
normalized_string = input_string.replace(" ", "").lower()

# Checking if the string is a palindrome
if normalized_string == normalized_string[::-1]:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
