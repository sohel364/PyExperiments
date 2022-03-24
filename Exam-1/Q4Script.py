BASECURRENCY = 'BDT'
def Rate(currencyName) :
    return int(input(currencyName + ' Rate please : '))

def Convert(amountToConvert, convertToCurrentname) :
    return amountToConvert / Rate(convertToCurrentname)

def PrintResult(fromCurrencyName, toCurrencyName, amount) :
    print(f"{fromCurrencyName} : {amount} = {Convert(amount, toCurrencyName)}" + f" {toCurrencyName}")

if(__name__ == '__main__') :
    op =''
    while True :
        try :
            print('Basic Currency converter.')
            amount = int(input(f'Please enter the {BASECURRENCY} amount to Convert: '))
            print(f"Convert BDT {amount}  to (example type: 1 for GBP conversion): \n 1. GBP(Pound) \n 2. USD \n 3. Euro \n")
            op = input('Please enther the currency you want to convert to : ')
            rate = 0
            if op == '1' :             
                PrintResult(BASECURRENCY, 'GBP', amount)
            elif op == '2' :
                PrintResult(BASECURRENCY, 'USD', amount)
            elif op == '3' :
                PrintResult(BASECURRENCY, 'Euro', amount)
            else :
                print ('Invalid choice. Please try again!')
                break
        except Exception as e:
            print ('Something is wrong App exited. Error : ' + str(e))
            break