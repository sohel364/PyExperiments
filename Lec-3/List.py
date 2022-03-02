##compare with user defined com funciton
def cmp(a, b):
    return (a > b) - (a < b) #
l1, l2  = [1,2,3,4], [1,2,3,4]
#with the defined comapre function
print(cmp(l1, l2))
#with the == operaiton
print(l1==l2)

## Let's know how lamda works
#let's define a function
def Add(a, b) :
    return a + b

#let's use Add it
print('Add using function : ' + str(Add(12, 13)))


# What is a lamda : A lamda is a short block of code which takes in parameter and returns value.
#It's like methods, but they do not need a name and they can be implemented right in the body of a method
# parameter -> expression

func = lambda a, b: a+b

print('Add Using lamda : ' + str(func(12, 13)))

#Reduce function
#Reference https://www.geeksforgeeks.org/reduce-in-python/

