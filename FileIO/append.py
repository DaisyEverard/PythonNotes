# LONG VERSION - APPEND
myFile = open("./scratchpad.txt", "a")
try:
    myFile.write("Append me number 1!\n")
finally:
    myFile.close

# The try/finally means the file always gets closed even if there is an error
# when writing to it

# SHORT VERSION - APPEND
with open("./input.txt", "a") as myFile:
    myFile.write("Append me number 2!\n")

# The with keyword is equivalent to the try/finally in the long version