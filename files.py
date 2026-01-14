file=open("f1.txt","r")
content=file.readline()
content1=file.readlines()
print(content)
print(content1)
file.close()

file=open("f1.txt","a")
file.write("\n New line added")
file.close()

file=open("f1.txt","w")
file.write("this is my write example")
file.close()