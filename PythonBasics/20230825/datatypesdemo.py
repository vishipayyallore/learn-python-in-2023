# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

age = 20
print("Age: ", age, "Type: ", type(age))

name = "John"
print("Name: ", name, "Type: ", type(name))

salary = 1000.0
print("Salary: ", salary, "Type: ", type(salary))

complex_number = 1 + 2j
print("Complex Number: ", complex_number, "Type: ", type(complex_number))

hobbies = ["Reading", "Writing", "Coding"]
print("Hobbies: ", hobbies, "Type: ", type(hobbies))

hobbies = ("Reading", "Writing", "Coding")
print("Hobbies: ", hobbies, "Type: ", type(hobbies))

range_numbers = range(10)
print("Range Numbers: ", range_numbers, "Type: ", type(range_numbers))

dictionary = {"name": "John", "age": 20}
print("Dictionary: ", dictionary, "Type: ", type(dictionary))

set_numbers = {1, 2, 3, 4, 5}
print("Set Numbers: ", set_numbers, "Type: ", type(set_numbers))

hobbies = frozenset({"Reading", "Writing", "Coding"})
print("Hobbies: ", hobbies, "Type: ", type(hobbies))

is_active = True
print("Is Active: ", is_active, "Type: ", type(is_active))

binary_data = b"Hello"
print("Binary Data: ", binary_data, "Type: ", type(binary_data))

binary_array = bytearray(5)
print("Binary Array: ", binary_array, "Type: ", type(binary_array))

memory_view = memoryview(bytes(5))
print("Memory View: ", memory_view, "Type: ", type(memory_view))

none_type = None
print("None Type: ", none_type, "Type: ", type(none_type))
