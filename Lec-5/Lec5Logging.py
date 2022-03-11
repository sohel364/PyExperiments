import logging
import sys
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(levelname)s - %(message)s')

a = input('Enter no :')
b = input('Enter no :')

if(a.isdigit() == False or b.isdigit() == False) :
    logging.critical('user input is not digit')
    sys.exit()

print(int(a)+int(b))
