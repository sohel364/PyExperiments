# Input first number
x = input('Please enter 1st number : ')
x = int(x)

# Input second number
y = input('Please enter 2nd number : ')
y = int(y)

# operation input
operation_type = input('Please select operation +, -, *, / : ')
if operation_type == '+' :
    print(x + y)
if operation_type == '-' :
    print(x - y)
if operation_type == '*' :
    print(x * y)
if operation_type == '/' :
    print(x / y)