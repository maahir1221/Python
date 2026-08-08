f=open("example.txt","w")
f.write("hello")
f.close()
f=open("example.txt","r")
data=f.read()
print(data)

# file management is used so that we can access and edit text file with help of code
# NOTE: The file management only works for text files, It can create, edit and open file with txt extension !

# Here open is to create or access a file.
# syntax is open("File name", "Mode")
# in the open, we need to add file name and the mode we want to use.
# following are different modes:
# 1. r is for read only.
# 2. w is for writing completely new file
# 3. a is for appending a file
# 4. r+ is for read and write
# 5. w+ is for read and write (Overwrites existing file)
# 6. a+ is for read, write and append

# variable.write is a place where you will type in what you want in the text file
# varible.close() is necessary whenever the file is open in order to close it and ensuring that you have finalized the edits.