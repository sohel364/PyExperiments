consoleStr = 'We are going to translate the word "Moon" as per your selection. \nPlease make your choice :\n1. Bengali \n2. Spanish \n3. Arabic'

if(__name__ == '__main__') :
    op =''
    while True :
        try :
            print(consoleStr)
            op = input()
            if op == '1' :
                print('চাঁদ')
            elif op == '2' :
                print('Luna')  
            elif op == '3' :
                print('القمر')
            else :
                print ('Invalid choice. Bye bye.')
                break
        except:
            print ('Invalid choice. Bye bye.')
            break