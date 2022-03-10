# This program demonstrate how to keep the program running by a user's choice
if(__name__ == '__main__') :
    op = ''
    while op != "entry" or  op != "search":
        op = input('entry or search\n')    
        if op == 'entry' :
            print("entrying....")
        elif op == 'search' :
            print("searchin...")            
        else :
            print ('Bye bye..')
            break