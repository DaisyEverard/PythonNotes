class Person():
    def __init__(self, age = "50"):
        self.age = age
        self.__private_variable = "I start with double underscore"
        self._non_public_instance_variable = "I start with a single underscore"

    def get_private_variable(self) -> str:
        return self.__private_variable
    
    def __private_method(self) -> None:
        print("I'm private")



def main():
    person = Person(40)

    print(person.age) # this will print 

    print(person._non_public_instance_variable)
    # this works because a single underscore is not functional,
    # it's just used to tell developers it's private

    ### print(person.__private_variable)
    # you can't directly access the private variable

    print(person.get_private_variable()) # access via a getter

    person.__private_variable = "a new value"
    print(person.__private_variable)
    # This now works because you've overwritten the value.
    # Don't do this, use a getter


main()