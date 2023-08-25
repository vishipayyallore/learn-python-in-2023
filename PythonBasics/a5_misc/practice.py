import sys


while True:
    try:
        x = int(input("Please enter a number: "))
        z = x + y
    except (TypeError, NameError, ValueError):
        print("Oops!  That was no valid number.  Try again...")
        print("Error Infor:", sys.exc_info())
        # raise
        break
