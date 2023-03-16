import time

# Define the arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'num2 cannot be zero :('
    else:
        return x / y

name = input("Hi, I'm calculator. What's your name? ")
print('Hello ' + name)
print('One moment please....')
time.sleep(1)

# Take input from the user
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Please try again.")

# Display the available operations
choice = input("What do you want to do with the numbers (+, -, *, /): ")
print('Processing...')
time.sleep(2)

# Perform the selected operation and display the result
if choice == '+':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '/':
    result = divide(num1, num2)
    if result is None:
        print("Cannot divide by zero.")
    else:
        print(num1, "/", num2, "=", result)
else:
    print("Invalid task.")

print('Thank you for using calculator')
