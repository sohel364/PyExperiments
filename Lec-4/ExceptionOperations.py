#key notes from w3schools
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
import traceback


try:
    print(something)
except:
    print("An excception!")

finally:
    print("Finished!")


#Raising an error and catch it
x = 100
try:
    if x == 100:
        raise Exception("Wrong data type!")
except:
    print(traceback.print_exc())