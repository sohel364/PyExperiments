# Function to check if a character is vowel
def IsVowel(ch) :
    return True if(
                    ch == 'A' or ch == 'a' or 
                    ch == 'E' or ch == 'e' or 
                    ch == 'I' or ch == 'i' or 
                    ch == 'O' or ch == 'o' or 
                    ch == 'U' or ch == 'u') else False

# The main function
if(__name__ == '__main__') :
    while True :
        try:
            word = input('Please enter the word to check vowel count : ')
            vowelCount = 0
            for char in word:
                if IsVowel(char) :
                    vowelCount +=1

            print(vowelCount)
        except:
            print('Bye bye')
            break