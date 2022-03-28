from AccessModifier import ClassA

if(__name__=='__main__'):
        ObjectofA = ClassA.A() 
        ObjectofA.funcPublic()
        #ObjectofA.__functionPrivate() # __functionPrivate s not known attribute
        ObjectofA.CallBothPublicAndPrivate()
        ObjectofA._A__functionPrivate() # # Calling the private member 
                                        # # through name mangling