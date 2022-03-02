# With if else considering Case
ch = input("Enter a character: ")
if(ch == 'A' or ch == 'a' or 
    ch == 'E' or ch == 'e' or 
    ch == 'I' or ch == 'o' or 
    ch == 'O' or ch == '0' or 
    ch == 'U' or ch == 'u') :

    print('You input character is a vowel!')
else :
    print('Your input character is not a vowel!')


# Trying by taking input charcter to lower case
print('Try by converting to lower case')

ch.lower() #converts input to lower case

if(ch == 'a' or ch == 'e' or 
   ch == 'i' or ch == 'o' or ch == 'u') :
      print('You input character is a vowel!')
else :
    print('Your input character is not a vowel!')