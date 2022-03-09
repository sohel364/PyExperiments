
import sys
import module_dictionary
# from readline import insert_text


# l = []
# for x in range(1,6) :
#     a = int (input('Please enter a number : '))
#     l.append(a)
# print(l)

# s = int(input('Please enter a number to search : '))

# for i in l :
#     if i == s :
#         print('result found ', i)

# 1. insert
# 2. search
# 3. update
# 4. delete

#Dictionary (Eng to Ben dictionary)
"""
asdasdas
asdasda
"""
'''
asasd
'''

# myDictionary = {} # decalre a empty dictionary
# d_file = 'd_data.csv'

# def prepare_dictionary_file (d_file) :
#     fobj = open(d_file, 'a') # 'r'->read / w- write ; a--> append operation
    
#     for x in range(0,4):
#         k = int(input('key please :'))
#         v = input('value please :')
#         myDictionary[k] = v
        
#         str_val = str(k) + ',' + v +'\n'
#         fobj.write(str_val)
#     fobj.close

#     print(myDictionary)

# def search_word(d_file) :    
#     fobj = open(d_file, 'r')
#     for item in fobj.readlines() :
#         print(item)
#         l1 = item.split(',') # l1[0]
#         #print(l1[0], l1[1])
#         myDictionary[l1[0]] = l1[1]
#     fobj.close()
#     print(myDictionary)

#     s = input('search key please :')
#     print(d[s])

# res=myDictionary.get(s, 'Sorry Not Found')
# print(res)

if(__name__ == '__main__') :
        op = input('entry or search\n')
        dictionaryInstance = module_dictionary.Dictionary('d_data.csv')
        if op == 'entry' :
            dictionaryInstance.prepare_dictionary_file()
        #if(op == 'search') :
            dictionaryInstance.search_word()
        #else :
         #   print ('not a valid choice')