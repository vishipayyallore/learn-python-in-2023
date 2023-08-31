import sqlite3

connection = sqlite3.connect('./data/employees.db')

"""
create_table = 'CREATE TABLE employees (ID INT PRIMARY KEY     NOT NULL, NAME TEXT NOT NULL);'

connection.execute(create_table, )
"""

insert_data = 'INSERT INTO employees values (105, \'Manas\'); '
connection.execute(insert_data)

insert_data = 'INSERT INTO employees values (106, "Misbah"); '
connection.execute(insert_data)

select_data = 'SELECT * FROM employees;'
datasets = connection.execute(select_data)

for id, name in datasets:
    print(id, name)

connection.commit()
connection.close()

print("Contenst saved to database successfully")
