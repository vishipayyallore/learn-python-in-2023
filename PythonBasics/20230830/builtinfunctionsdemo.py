# Built in functions demo

print('dir() = ', dir())

print('__name__ = ', __name__)
print('dir(__name__) = ', dir(__name__))

print('__builtins__ = ', __builtins__)

print('dir(__builtins__)', __builtins__)

output = dir(__builtins__)
print('dir(__builtins__) as output = ', output)

print('ArithmeticError = ', ArithmeticError)

# # abs() - returns the absolute value of a number
# print(abs(-45))

# # all() - returns true if all items in an iterable object are true
# print(all([1, 2, 3, 4]))

# # any() - returns true if any item in an iterable object is true
# print(any([0, 1, 2, 3]))

# # ascii() - returns a readable version of an object. Replaces none-ascii characters with escape character
# x = 'My name is Ståle'
# print(ascii(x))

# # bin() - returns the binary version of a number
# print(bin(5))

# # bool() - returns the boolean value of the specified object
# print(bool(0))

# # bytearray() - returns an array of bytes
# print(bytearray(5))

# # bytes() - returns a bytes object
# print(bytes(5))

# # callable() - returns true if the specified object is callable, otherwise false
# x = 5
# print(callable(x))

# # chr() - returns a character from the specified Unicode code
# print(chr(97))

# # classmethod() - converts a method into a class method
# class Person:
#     age = 25

#     def printAge(cls):
#         print('The age is:', cls.age)

# # create printAge class method
# Person.printAge = classmethod(Person.printAge)
# Person.printAge()

# # compile() - returns the specified source as an object, ready to be executed
# x = compile('print(55)', 'test', 'eval')
# exec(x)

# # complex() - returns a complex number
# print(complex(5))

# dir() # returns a list of the specified object's properties and methods
# print(dir())

# # divmod() - returns the quotient and the remainder when argument1 is divided by argument2
# print(divmod(5, 2))

# # enumerate() - takes a collection (e.g. a tuple) and returns it as an enumerate object
# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)

# __builtins__.enumerate(x)
