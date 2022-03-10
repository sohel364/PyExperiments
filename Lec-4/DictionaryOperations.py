
import sys
import Module_dictionary

# The Main function : Program starts from here. It's a system function
if(__name__ == '__main__') :
    dictionaryInstance = Module_dictionary.Dictionary('d_data.csv') # Create Object of Dictionary class from Module_dictionary
    programOptions = ["entry", "print", "searchkey", "searchvalue"] # the operations this program can perform
    op = '' # op is going to hold the choice user types
    while op not in programOptions:
        op = input('Please choose your operation {}'.format(programOptions))
        if op == 'entry' :
            dictionaryInstance.prepare_dictionary_file()
        elif op == 'print' :
            dictionaryInstance.printDictionaryItems()
        elif op == 'searchkey' :            
            dictionaryInstance.search_dictionaryItemsByKey(int(input("What is the key you are looking  for ? ")))
        elif op == 'searchvalue' :
            dictionaryInstance.search_dictionaryItemByValue(input("What is the value you are looking  for ? "))

        else :
            print ('Bye bye..')
            break