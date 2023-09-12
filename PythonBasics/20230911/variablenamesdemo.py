# A Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# A Variable name cannot start with a number
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# Variable name must start with a letter or the underscore character

# Camel Case
userName = "Sri Varu"
print("Hello", userName, type(userName))

# Pascal Case
UserName = "Sri Varu"
print("Hello", UserName, type(UserName))

# Snake Case
user_name = "Sri Varu"
print("Hello", user_name, type(user_name))

# Many Values to Multiple Variables
user_name, user_age, user_salary = "Sri Varu", 21, 100000.00
print("Hello", user_name, "you are", user_age, "years old and make", user_salary, "dollars per year", type(user_name), type(user_age), type(user_salary))