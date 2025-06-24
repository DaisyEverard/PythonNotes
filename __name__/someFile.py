from otherFile import isNameMain

print("someFile __name__: ", __name__)
# This will be __main__ if you run this file, but the print from otherFile
# will tell you that __name__ there is now otherFile, the same name as the file

print("someFile isNameMain: ", isNameMain())
# This will be false as, although you are calling isNameMain in the __main__ file
# it is still being run in otherFile