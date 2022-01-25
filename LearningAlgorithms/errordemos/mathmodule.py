"""Module to have basic math functions

"""

import sys


def add_two_numbers(value1: int, value2: int) -> int:
    """Method to add two add_two_numbers

        ARGUMENTS: 
            Value1: first value
            Value2: second value
    """

    try:
        return value1 + value2
    except TypeError as error:
        print('Error at add_two_numbers()', error)
    except:
        print('General Error at divide_two_numbers()')


def divide_two_numbers(value1: int, value2: int) -> float:
    """Method to add two add_two_numbers

        ARGUMENTS: 
            Value1: first value
            Value2: second value
    """

    try:
        return value1 / value2
    except ZeroDivisionError as error:
        print('ZeroDivisionError at divide_two_numbers()', error)
    except TypeError as error1:
        print('TypeError at divide_two_numbers()', error1)
    except:
        print('General Error at divide_two_numbers()', sys.exc_info())
