from mathmodule import *

divide = divide_two_numbers(1, '0')
print(f'Divide: {divide}')

add = add_two_numbers(1, 2)
print(f'Addition: {add}')

try:
    add = add_two_numbers(1, 's')
    print(f'Addition: {add}')
except:
    print('General Error at add_two_numbers()')

divide = divide_two_numbers(1, 0)
print(f'Divide: {divide}')

divide = divide_two_numbers(1, '0')
print(f'Divide: {divide}')
