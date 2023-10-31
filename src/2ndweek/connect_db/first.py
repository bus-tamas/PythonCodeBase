import mysql.connector

def connectToDatabase(user,password,host,database):
    mydb = mysql.connector.connect(
        user = user,
        password = password,
        host = host,
        database = database
    )
    return mydb

mydb = connectToDatabase('root', '1234', 'localhost', 'c371dataanalysis')
my_cursor = mydb.cursor()
query = "show tables"
my_cursor.execute(query)

tables = my_cursor.fetchall()

for table in tables:
    print(table[0])


'''
create_query = "CREATE TABLE IF NOT EXISTS test1 (id int auto_increment primary key, name varchar(50))"
'''