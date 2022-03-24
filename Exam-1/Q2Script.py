# Function to populate the next odd numbers
def PopulateNextOdds(num) :
    listOfOdds = []
    while len(listOfOdds) <= 9 :
        num +=1 # we want to decide from the next numbers
        if num % 2 == 0 :
            pass
        else :
            listOfOdds.append(num)

    return listOfOdds

if(__name__ == '__main__') :
    while True:
        op = input('Please enter a number : ' )
        if(op.isdigit()) :    
           print(PopulateNextOdds(int(op)))

        else :    
            print ('Invalid input Bye bye.')
            break