import pymssql

conn = pymssql.connect(server='YourServer.database.windows.net',
                       user='YourUserName', password='YourPassword', database='YourDatabase')

cursor = conn.cursor()
cursor.execute('SELECT * from dbo.Professors;')
row = cursor.fetchone()
while row:
    print(str(row[0]), str(row[1]), str(row[2]), str(
        row[3]), str(row[4]), str(row[5]), str(row[6]))
    row = cursor.fetchone()


cursor.execute('SELECT * from dbo.Products;')
row = cursor.fetchone()
while row:
    print(str(row[0]), str(row[1]), str(row[2]), str(
        row[3]), str(row[4]))
    row = cursor.fetchone()


conn.close()
