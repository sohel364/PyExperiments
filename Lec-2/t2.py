
#check type
a = 0
print(type(a))
name = 'Dhaka'
print(type(name))
b = 3.8
print(type(b))

c1=22
c1='22' # when comes froim user input in terminal
c2 = int(c1)
type(c1)
type(c2)

#Reserved Keyword python
#knowing about the library functions

#c= input() // doesnt work from script but works in shell
#print(c)
#system.stdinput

#problem :
    #< 4.5 ==> x
    #>= 4.5 ==> y
    #5      ===>z

#Problem : from user's input ( a single character), find if vowel or not

# c= input('please enter single character : ')
# if c== 'a' :
#     print('vowel')
# elif c== 'e' :
#     print('vowel')    
# elif c== 'i' :
#     print('vowel')    
# elif c== 'o' :
#     print('vowel')            
# elif c== 'u' :
#     print('vowel')
# else:
#     print('Not a vowel')

# Prob : find a user's grade from his cgpa
    #A+: 80%
    #A : 70-79
    #B

# type of problems : if else ladder



#in multiple line
x = input('please enter 1st number : ')
x = int(x)

y = int (input('please enter 2nd number :')) # in single line

operation_type = input('Please enter operation type (+, -, *, /) : ') # home work rest of the operators

if operation_type == '+' :
    print(x + y)
