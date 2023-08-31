# Built in functions input() and print()

user_name = input("Enter your name: ")
print("Hello", user_name, type(user_name))

user_age = input("Enter your age: ")
print("You are", user_age, "years old", type(user_age))

user_age = int(user_age)
print("You are", user_age, "years old", type(user_age))

favortie_number = input("Enter your favorite number: ")
print("Your favorite number is", favortie_number, type(favortie_number))

favortie_number = int(favortie_number)
print("Your favorite number is", favortie_number, type(favortie_number))

favorite_color = input("Enter your favorite color: ")
print("Your favorite color is", favorite_color.upper(), type(favorite_color))
