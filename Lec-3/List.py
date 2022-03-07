#Initialize and Test by print : List of diffrent data types
from ast import While


print('Let\'s see diffrent types of List :')
EmptyList = [] #empty list
print("An empty List: {0}".format(EmptyList)) # Formatted string

ListOfSameType = [1,2,3,4,5] #List of intgers
print('List of similar types of item : {0}'.format(ListOfSameType))

ListOfMixedType = [0.0, 1.2, 3, 4, 5, 'globe', 'sky', bool] # List of mixed data types
print('List of mixed type of item : {0}'.format(ListOfMixedType))

NestedList = [1, 'unbrella', [0.0, 0.1, 0.2, 10], [], ['apple', 'grapes', [1,2,3.0]]] # A nested List
print('List of mixed type of item : {0}'.format(NestedList))

# List slicing
# Basic syntax:
#list[start:stop:step]

# Note, Python is 0-indexed
# Note, start is inclusive but stop is exclusive
# Note, if you leave start blank, it defaults to 0. If you leave stop
# 	blank, it defaults to the length of the list. If you leave step
# 	blank, it defaults to 1.
# Note, a negative start/stop refers to the index starting from the end
# 	of the list. Negative step returns list elements from right to left 

# Initialize list
Lst = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(Lst[::]) # here start, step, stop are empty.

# Loops
#While loop with break condition, pass statement
i = True
j = 0
name = ''
yesNo = 0
while i:
    print(i)        
    if j == 10 :
        print('Ended at : {0}'.format(j))
        break
    if j == 4 :
        pass
    if j == 5 :        
       name = input('Your name please : ')
       print(f"We reached Mr.{name}")
       yesNo = input('Do you like to end the loop? Type 1 to end and 0/anything else to continue : ')
       if yesNo == 1 :
            print('Got continue command after the input at : {0}'.format(j))
       else :
            pass

    j += 1



ListOfTesting1, ListForTesting2, ListEmpty = [1, 2, 3, 5], [3,5,6,7,8], []

print(ListOfTesting1, ListForTesting2) # Simple print full items

# for loop print items
for num in ListOfTesting1 :
    print(num)

for _ in ListForTesting2 : 
    print(f'hello', _)