"""
File I/O

'w' --> Write only mode
'r' --> Read only mode
'r+' --> Read and Write Mode
'a' --> Append mode

"""
# *************** 56: How to write data to a file

myFamilyName= ['Chaitanya', 'Ambica', 'Yashvir', 'Dhiyanshi']
myFamilyFile= open("myFamilyNames.txt", "w") # here the path of the file is not given that means, the file will be created under the working working directory.

for i in myFamilyName:
    myFamilyFile.write(str(i)+" ") # in double quotes space is given. If we give \n  a new line will be created after each and every name. \n is carriage return.

myFamilyFile.close()


# ************** 57: How to read a file
"""
File I/O
Reading a file ---> .read()
Reading line by line ---> .readline()
"""

myFamilyFile= open("myFamilyNames.txt", 'r')
print(str(myFamilyFile.read()))
myFamilyFile.close()


# ************** 58: File handling using 'With' and 'As' keywords
"""
With / As Keywords
"""
print("With As Write Start")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is an example of with as write / read")

print()
print("With as read start")
with open("withas.txt", "r") as with_as_read:
    print(str(with_as_read.read()))

