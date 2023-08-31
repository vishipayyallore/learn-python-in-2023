# Variables Demo
# Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type and can even change type after they have been set.

user_name = "Sri Varu"
print("Hello", user_name, type(user_name))

user_age = 21
print("You are", user_age, "years old", type(user_age))

user_salary = 100000.00
print("You make", user_salary, "dollars per year", type(user_salary))

is_manager = True
print("Are you a manager?", is_manager, type(is_manager))

user_address = "123 Main Street, Anytown, USA"
print("Your address is", user_address, type(user_address))

# Casting
x = int(1)   # x will be 1
print('x', x, type(x))

y = int(2.8)  # y will be 2
print('y', y, type(y))

z = int("3")  # z will be 3
print('z', z, type(z))

x = str(3)    # x will be '3'
print('x', x, type(x))

y = int(3)    # y will be 3
print('y', y, type(y))

z = float(3)  # z will be 3.0
print('z', z, type(z))

# Single or Double Quotes
user_name = 'Sri Varu'
print("Hello", user_name, type(user_name))

user_name = "Sri Varu"
print("Hello", user_name, type(user_name))

# Case Sensitive
a = 4
print("a =", a, type(a))

A = "Sally"
print("A =", A, type(A))
