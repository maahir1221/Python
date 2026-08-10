import os

os.getcwd()
print(os.getcwd())
print("Show directory")

os.mkdir("Heyram/abcd")


os.rmdir("Heyram/abcd")
print("Directory Delete")

os.listdir("Heyram")
print("List Directory", os.listdir("D://Python/basic"))


# Here I have imported os first.
# os.getcwd means that it is asking os to bring current working directory
# now os.rmdir means remove "EMPTY" directory. Please note the directory should be entirely empty for this to work
# os.listdir() is a python function from os module.
# it will return a list of all the files and directories in the given path
# Here "abcd" directory will be created inside heyram first and will be removed since it was empty