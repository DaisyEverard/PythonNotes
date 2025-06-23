# Works on arrays, tupples, and string (indexable objects)
myArray = [100,101,102,103,104,105,106,107,108,109]
myTupple = (0,1,2,3,4,5,6,7,8,9)
myString = "abcdefghij"

# start index inclusive
print(myArray[2::])

# end index exclusive
print(myTupple[:5:])

# print backwards by using a step of -1
print(myString[::-1])