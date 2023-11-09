import mysql.connector

def connectToDatabase(host,user,password,database):
    connector = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connector

connection = connectToDatabase("localhost","root","123","c371dataanalysis")

cursor = connection.cursor()

create_table = "create table if not exists test2(id int primary key auto_increment, name varchar(255), age int, othersmthng int)"

try:
    cursor.execute(create_table)
except Exception as e:
    print(e)
    print("Unsuccessful connection to database")