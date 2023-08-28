# Functions in Python. To run this file, type "python functiondemo1.py" in the command prompt
# say_hello(name) is to greet the user with the name provided

# Function definition. name is a parameter
def say_hello(name):
    print("Hello ", name)


# Function call or Invocation. "John" is an argument, similarly "Mary", "Peter" and "Tom"
say_hello("John")
say_hello("Mary")
say_hello("Peter")
say_hello("Tom")


def add_two_numbers(a, b):
    return a+b

num1 = 10
num2 = 20

# Function call or Invocation. num1 and num2 are arguments
print("Sum of", num1, "+", num2, "=", add_two_numbers(num1, num2))

