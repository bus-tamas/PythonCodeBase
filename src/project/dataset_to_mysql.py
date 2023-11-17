import mysql.connector
import pandas as pd 
from datetime import datetime
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

csv_file_path = os.path.join(current_dir, 'Superstore.csv')

df = pd.read_csv(csv_file_path, encoding='latin1')

#print(df.head())

def connectToDatabase(host,user,password,database):
    connector = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connector

connection = connectToDatabase("localhost","root","1234","c371dataanalysis")

cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS Superstore (
    `Row ID` INT,
    `Order ID` VARCHAR(255),
    `Order Date` DATE,
    `Ship Date` DATE,
    `Ship Mode` VARCHAR(255),
    `Customer ID` VARCHAR(255),
    `Customer Name` VARCHAR(255),
    `Segment` VARCHAR(255),
    `Country` VARCHAR(255),
    `City` VARCHAR(255),
    `State` VARCHAR(255),
    `Postal Code` INT,
    `Region` VARCHAR(255),
    `Product ID` VARCHAR(255),
    `Category` VARCHAR(255),
    `Sub-Category` VARCHAR(255),
    `Product Name` VARCHAR(255),
    `Sales` FLOAT,
    `Quantity` INT,
    `Discount` FLOAT,
    `Profit` FLOAT
)
"""


try:
    cursor.execute(create_table_query)
    print("Table created successfully")
except Exception as e:
    print(e)
    print("Unsuccessful connection to the database")

for index, row in df.iterrows():
    order_date = datetime.strptime(row['Order Date'], '%m/%d/%Y').strftime('%Y-%m-%d')
    ship_date = datetime.strptime(row['Ship Date'], '%m/%d/%Y').strftime('%Y-%m-%d')

    row['Order Date'] = order_date
    row['Ship Date'] = ship_date

    insert_query = """
    INSERT INTO Superstore (`Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`,
        `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`,
        `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, tuple(row))

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Done")