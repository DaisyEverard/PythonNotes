def tuppleArg(*myTuple):
    for x in myTuple:
        print("func1: ", x)

tuppleArg(1,2,3,4)

# using a single asterisk in your paramter means the function
# will take multiple arguments for this when called and store them in a tuple
# -----------------------------

def dictionaryArg(**myDict):
    for x,y in myDict.items():
        print("Tuple: ", x, y)

dictionaryArg(one=1,two=2,three=3,four=4)

# A double askterisk stores the multiple values in a dictionary
# -----------------------------

def stringTuppleDict(myString, *myTuple, **myDictionary):
    print("string: ", myString)

    for x in myTuple:
        print("func1: ", x)

    for x,y in myDictionary.items():
        print("Dictionary: ", x, y)

stringTuppleDict("\n\ncombined Function:", "a", "b", "c", "d", one=1, two=2, three=3)
# When you combine multiple paramters like this it can get confusing so
# is generally best avoided or limited to one where necessary.
# The single argument parameters are put before the multiple argument ones