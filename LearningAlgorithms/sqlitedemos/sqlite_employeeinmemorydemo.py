import sqlite3

connection = sqlite3.connect(':memory:')
print("Opened database successfully")

create_table = 'CREATE TABLE students (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL);'
connection.execute(create_table)

insert_data = 'INSERT INTO students values (101, \'Shiva\');'
connection.execute(insert_data)

insert_data = 'INSERT INTO students values (102, \'Mathews\');'
connection.execute(insert_data)

insert_data = 'INSERT INTO students values (103, \'Misbah\');'
connection.execute(insert_data)

select_data = 'SELECT * FROM students;'
datasets = connection.execute(select_data)

# print(datasets)

# for row in datasets:
#     print(row)

for id, name in datasets:
    print(id, name)
