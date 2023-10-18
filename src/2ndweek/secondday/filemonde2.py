with open("example.txt","wb") as file:
    data = b'This is a binary \n file'
    file.write(data)

with open("example.txt","wb+") as file:
    data = b'This is a binary \n file 2nd time'
    file.write(data)

    file.seek(0)
    content = file.read()
    print("Write and read ", content)