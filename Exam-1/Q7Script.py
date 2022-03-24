# Lets print all next odds in a range
start = int(input('Start from : '))
if(start % 2 == 0) :
    for i in range(start+1, int(input('End at : ')), 2) :
        print(i)
else:
    for i in range(start+2, int(input('End at : ')), 2) :
        print(i)