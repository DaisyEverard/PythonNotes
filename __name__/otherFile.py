
def isNameMain():
    return __name__ == "__main__"

print("otherFile __name__: ", __name__)
# When top-level code is run
# (when the file you are running is in the root of the execution path)
# __name__ is set to __main__

print("otherFile isNameMain: ", isNameMain())
# This will print True if you run this file directly from the command line