def getdictionaryItems(fileName) :    
    fobj = open(fileName, 'r')
    itemList = []
    for item in fobj.readlines() :
        rowItems = item.split(',')
        itemList.append(int(rowItems[2].strip('\n')))
    fobj.close()  
    return itemList

itemList = getdictionaryItems('input_data.csv')
print(itemList)

#sort with sorted
print(sorted(itemList))
print(sorted(itemList, reverse=True))