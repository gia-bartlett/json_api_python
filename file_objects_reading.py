# File Objects

# method for opening files without a context manager (not recommended)
# when using this method we will ne to explicitly close it when done
# if you don't then you can end up with file leaks that run over the max file descriptors on system

# f = open("test.txt", "r")  #if file isn't in the same directory then the full path will be needed
# print(f.name)  # prints file name = test.txt
# print(f.mode)  # prints the mode the file is open in = r
#
# f.close() # closes the file

# opening with a context manager - don't need to worry about closing
with open("test.txt", "r") as f:  # --> f = open("test.txt", "r")

    # for line in f:
    #     print(line, end = "")  # this is memory efficient because it doesn't read the whole file at once

    # f_contents = f.read()  # .read reads the whole file
    # print(f_contents)  # prints the contents of the file

    # f_contents = f.readlines()  # .readlines produces a list of all the lines
    # f_contents = f.readline()  # grabs the first entry from a list of all the lines
    # print(f_contents)
    # if repeated with the same variable name it wil go on to the next index
    # but if given a new variable it will start over again
    # print statement needs to be repeated after each otherwise it will only print the last one

    # f_contents = f.read(100)  # first 100 characters of file
    # print(f_contents)

    # size_to_read = 10
    # f_contents = f.read(size_to_read)  # first 10 characters of file as set by variable
    # print(f.tell())  # what position we are in the file

    size_to_read = 10
    f_contents = f.read(size_to_read)  # first 10 characters of file as set by variable
    print(f_contents)
    f.seek(0)  # sets us back at 0 index
    f_contents = f.read(size_to_read)  # will start back at 0 because of .seek()
    print(f_contents)

    # while len(f_contents) > 0:
    #     print(f_contents, end = "*")  # will put in a * after every 10 characters
    #     f_contents = f.read(size_to_read)


print(f.closed)  # True --> meaning you have to work with the file from within the with open
