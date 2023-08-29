"""
Description: This program demonstrates how to define and call functions.
Date: 2021-08-29
Name: functiondemo.py
Author: Viswanatha Swamy
"""


def multiply_numbers(a, b):
    return a * b


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def divide_numbers(a, b):
    return a / b


# This function does not return a value. None is returned by default.
def say_hello():
    print("Hello, world!")


def main():
    print("This is a function demo.")
    print("The result of 4 * 5 is", multiply_numbers(4, 5))
    print("The result of 4 + 5 is", add_numbers(4, 5))
    print("The result of 4 - 5 is", subtract_numbers(4, 5))
    print("The result of 4 / 5 is", divide_numbers(4, 5))
    # None is returned by default.
    print("The result of say_hello() is", say_hello())


# Call the main function.
main()
