def getSurNameFromFullName(fullname):
    return fullname.split()[-1]

print(f"Surname is : {getSurNameFromFullName(input('Please enter your name : '))}")