import mysql.connector
def connectToDatabase(user,password,host,database):
    mydb = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )
    return mydb
mydb = connectToDatabase("root","1234","localhost","c371dataanalysis")
mycursor = mydb.cursor()
create_query = "CREATE TABLE IF NOT EXISTS test1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
mycursor.execute(create_query)
insert_query = "insert into test1 (name,age) values (%s,%s)"
name='dummy'
age=50
val = (name,age)
mycursor.execute(insert_query,val)
mydb.commit()
search_query = "select * from test1 where name = dummy"

#asd