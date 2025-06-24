with open("./input.txt", "r") as myFile:
    print(myFile.read()) # whole file
    myFile.seek(0)
    # the cursor will now be at the end of the file so we
    # need to reset it to the start

    print(myFile.read(1))
    print(myFile.read(5))
    print(myFile.read(5))
    # This reads x characters from where the cursor it
    myFile.seek(0)

    print(myFile.readline())
    # reads the whole line the cursor is on
    myFile.seek(0)

    print(myFile.readlines())
    # returns a list of lines