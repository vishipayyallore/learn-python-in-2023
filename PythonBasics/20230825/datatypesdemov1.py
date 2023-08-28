# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# String
name = str("John")
print("Name: ", name, "Type: ", type(name))

# Integer
age = int(20)
print("Age: ", age, "Type: ", type(age))

# Float
salary = float(1000.0)
print("Salary: ", salary, "Type: ", type(salary))

# Complex
complex_number = complex(1 + 2j)
print("Complex Number: ", complex_number, "Type: ", type(complex_number))

# List
hobbies = list(("Reading", "Writing", "Coding"))
print("List of Hobbies: ", hobbies, "Type: ", type(hobbies))

# Tuple
hobbies = tuple(("Reading", "Writing", "Coding"))
print("Tuple Hobbies: ", hobbies, "Type: ", type(hobbies))

# Range
range_numbers = range(10)
print("Range Numbers: ", range_numbers, "Type: ", type(range_numbers))

# Dictionary
dictionary = dict(name="John", age=36)
print("Dictionary: ", dictionary, "Type: ", type(dictionary))

# Set
set_numbers = set((1, 2, 3, 4, 5))
print("Set Numbers: ", set_numbers, "Type: ", type(set_numbers))

set_fruits = set(("apple", "banana", "cherry"))
print("Set Fruits: ", set_fruits, "Type: ", type(set_fruits))

# Frozen Set
hobbies = frozenset({"Reading", "Writing", "Coding"})
print("Frozen Set Hobbies: ", hobbies, "Type: ", type(hobbies))

# Boolean
is_active = bool(5)
print("Bool Is Active: ", is_active, "Type: ", type(is_active))

# Binary Data
binary_data = bytes(5)
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
