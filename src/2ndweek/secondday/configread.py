from decouple import config

database_host=config("DATABASE_HOST")
print(database_host)

""" import os

c = os.getcwd()
print(c)
os.chdir(r"C:\Users\Tamás\Desktop\Minden fájl\MS\Code\PythonCodeBase\src\2ndweek")
c = os.getcwd()
print(c)
directory = r"C:\Users\Tamás\Desktop\Minden fájl\MS\Code\PythonCodeBase\src\2ndweek"
folder = r"C:\Users\Tamás\Desktop\Minden fájl\MS\Code\PythonCodeBase\src\2ndweek\secondday\dummy"
os.rmdir(folder) """

import subprocess
with open(r"output.txt","wb") as f:
    subprocess.run(["python","filemode.py"],stdout=f,text=True)