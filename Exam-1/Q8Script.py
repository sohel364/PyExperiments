import CalculatorModule

if(__name__ == '__main__') :
    choice = int(input('To Test the basic calculator press 1 or press anykey to exit! :'))
    if(choice == 1):
      CalculatorModule.BasicCalculationFuncion()
    else:
        exit('Bye bye')

