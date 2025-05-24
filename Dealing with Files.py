#Creating a file path
#Importing the os module
import os
os.path.join("Users","Luis","Documents","Test.txt")
#The os.path.join() method joins one or more path components intelligently.
#The first argument is the directory, and the second argument is the file name.
#The os.path.join() method will add the correct path separator for the operating system.

#Opening a file, writing to it, and closing it
#The open() method is used to open a file.
#The first argument is the file name, and the second argument is the mode.
#The mode can be "r" for reading, "w" for writing, "a" for appending, and "x" for exclusive creation.
#The "w" mode will create a new file if it does not exist, or overwrite the existing file.
st = open("Test.txt", "w")
#The write() method is used to write to the file.
st.write("Hi there, this is a test Python file!")
st.close()
#The close() method is used to close the file.

#Another way to open a file is to use the with statement.
#The with statement will automatically close the file when the block is exited.
with open("sample.txt", "w") as f:
    f.write("Hello, Howard!")
#The with statement is used to wrap the execution of a block with methods defined by a context manager.

#Reading a file
#Use a with statement to open the file in read mode
#The syntax is the same as the write mode, but the mode is "r" instead of "w".
with open("sample.txt", "r") as f:
    #The read() method reads the entire file and returns it as a string.
    print(f.read())

#To save the read string to a variable, use the following syntax:
#In this example, we will save it to a list.
my_list = list()
with open("sample.txt", "r") as f:
    #We will use the append() method with f.read to add the string to the list.
    my_list.append(f.read())
print(my_list)
