# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Integer
age = 20
print("Age: ", age, "Type: ", type(age))

# String
name = "John"
print("Name: ", name, "Type: ", type(name))

# Float
salary = 1000.0
print("Salary: ", salary, "Type: ", type(salary))

# Complex
complex_number = 1 + 2j
print("Complex Number: ", complex_number, "Type: ", type(complex_number))

# List
hobbies = ["Reading", "Writing", "Coding"]
print("Hobbies: ", hobbies, "Type: ", type(hobbies))

# Tuple
hobbies = ("Reading", "Writing", "Coding")
print("Hobbies: ", hobbies, "Type: ", type(hobbies))

# Range
range_numbers = range(10)
print("Range Numbers: ", range_numbers, "Type: ", type(range_numbers))

# Dictionary
dictionary = {"name": "John", "age": 20}
print("Dictionary: ", dictionary, "Type: ", type(dictionary))

# Set
set_numbers = {1, 2, 3, 4, 5}
print("Set Numbers: ", set_numbers, "Type: ", type(set_numbers))

# Frozen Set
hobbies = frozenset({"Reading", "Writing", "Coding"})
print("Hobbies: ", hobbies, "Type: ", type(hobbies))

# Boolean
is_active = True
print("Is Active: ", is_active, "Type: ", type(is_active))

# Binary Data
binary_data = b"Hello"
print("Binary Data: ", binary_data, "Type: ", type(binary_data))

# Byte Array
binary_array = bytearray(5)
print("Binary Array: ", binary_array, "Type: ", type(binary_array))

# Memory View
memory_view = memoryview(bytes(5))
print("Memory View: ", memory_view, "Type: ", type(memory_view))

# None Type
none_type = None
print("None Type: ", none_type, "Type: ", type(none_type))
