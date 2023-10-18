file = open("test.txt", "a+")
#file = open("test.txt", "w+")
#file = open("test.txt", "r+")

file.write("Hello World!")
file.write(b"Hello World!")

file.seek(0)

data = file.read()

print(data)

file.close()