
# with open("test.txt", "r") as f:
#     f.write("Test")  # this will create an error because the file is open in "r" read mode

# with open("test2.txt", "w") as f:  # if the filename exist it will overwrite it and if it doesn't it will create it
#     f.write("Test")  # Test is written in test2.txt file
#     f.seek(0)
#     f.write("t")  # big T will be overwritten with little t

with open("test.txt", "r") as rf:  # we have opened test for reading
    with open("test_copy.txt", "w") as wf:  # we have created a file for writing
        # for line in rf:
        #     wf.write(line)  # iterate through and write each line to the new file
        chunk_size = 10  # choose a size of data
        rf_chunk = rf.read(chunk_size)  # read in a chunk of 10 characters
        while len(rf_chunk) > 0:  # create a loop that will write these chunks to the copy
            # until it gets to the end of the chunk
            wf.write(rf_chunk)  # write chunk to copy file
            rf_chunk = rf.read(chunk_size)  # read in the next chunk otherwise it'll be an infinite loop



