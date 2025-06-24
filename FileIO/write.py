myFile = open("./scratchpad.txt", "w")
# w is write mode

# r - read - pointer at beginning - default for open()
# r+ - read and write - pointer at beginning
# w - write - pointer at beginning - overwrites existing file or
#    creates a new one if one doesn't exist
# w+ - write + read
# a - append - pointer at end of existing file. Creates new one if not exists

myFile.write("this is something I wrote\n")

for i in range(1,5):
    myFile.write("%d\n" %i)
    # need to format number to string

myFile.close()
# after you close a file no more modifications can be made
# until it's opened again