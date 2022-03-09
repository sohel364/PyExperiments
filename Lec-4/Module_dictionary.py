class Dictionary : 
    fileName = ""
    theDictionary = {}
    def __init__(self, fName) :
        self.fileName = fName
    
    def prepare_dictionary_file (self) :        
        fobj = open(self.fileName, 'a') # 'r'->read / w- write ; a--> append operation        
        for x in range(0,4):
            k = int(input('key please :'))
            v = input('value please :')
            self.theDictionary[k] = v
            
            str_val = str(k) + ',' + v +'\n'
            fobj.write(str_val)
        fobj.close
        print(self.theDictionary)

    def search_word(self) :    
        fobj = open(self.fileName, 'r')
        for item in fobj.readlines() :
            print(item)
            # rowItems= item.split(',') # l1[0]
            #print(l1[0], l1[1])
            #self.theDictionary[l1[0]] = l1[1]
        fobj.close()
        #print(self.theDictionary)

        # s = input('search key please :')
        # print(self.theDictionary[s])

        # res=self.theDictionary.get(s, 'Sorry Not Found')
        # print(res)
# if(__name__=='__main__') :
#     print('i am in main')
