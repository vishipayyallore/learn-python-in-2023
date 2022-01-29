import sqlite3

connection = sqlite3.connect('./data/studentsv1.db')

c = connection.cursor()

# get the count of tables with the name
c.execute(
    '''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='students';''')

create_table = '''CREATE TABLE students (ID INT PRIMARY KEY     NOT NULL, NAME TEXT NOT NULL);'''

# if the count is 1, then table exists
if c.fetchone()[0] == 0:
    print('Table does not exists.')
    connection.execute(create_table, )


id = int(input('Enter Id: '))
name = input('Name: ')
insert_data = f'INSERT INTO students values ({id}, \'{name}\');'
connection.execute(insert_data)

id = int(input('Enter Id: '))
name = input('Name: ')
insert_data = f'INSERT INTO students values ({id}, \'{name}\');'
connection.execute(insert_data)

print("Data Saved into Database Successfully")

select_data = '''SELECT * FROM students;'''
datasets = connection.execute(select_data)

for id, name in datasets:
    print(id, name)

connection.commit()
connection.close()
