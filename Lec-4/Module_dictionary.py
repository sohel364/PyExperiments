#Class Dictionary
class Dictionary : 
    fileName = ""  # the file name
    theDictionary = {} # empty dictionry
    def __init__(self, fName) : 
        self.fileName = fName

    #Prepares the dictionary
    def prepare_dictionary_file (self) :        
        fobj = open(self.fileName, 'a') # 'r'->read / w- write ; a--> append operation        
        for x in range(0,4):
            k = int(input('key please :'))
            v = input('value please :')
            self.theDictionary[k] = v
            
            str_val = str(k) + ',' + v +'\n'
            fobj.write(str_val)
        fobj.close()
        print(self.theDictionary)
    
    #Read the file and get the dictionary items
    def get_dictionaryItems(self) :    
        fobj = open(self.fileName, 'r')
        itemList = {}
        for item in fobj.readlines() :
            #print(item)
            rowItems = item.split(',') # l1[0]
            #print(rowItems)            
            #print(rowItems[0], rowItems[1])        
            itemList[int(rowItems[0])] = rowItems[1]
        fobj.close()  
        #print(itemList)
        return itemList
    
    def printDictionaryItems(self) :
        print(self.get_dictionaryItems())

    #Search dictionary item by key
    def search_dictionaryItemsByKey(self, key) :        
        if key in self.get_dictionaryItems() :
            print("Key found!" + "The associated value : {}".format(self.get_dictionaryItems()[key]))
        else :
            print("Invalid item!")
    
    #Search dictionary value
    def search_dictionaryItemByValue(self, value) :        
        if value in self.get_dictionaryItems().values() :
            print("Found The Value {}!".format(value))
        else :
            print("The Value {} not found!".format(value))