s=input("enter the data to be written in file:")
file=open("cse.txt","w")

file.write(s)
print("file created successfully")
file.close()