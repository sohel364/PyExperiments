from ast import Lambda
from AccessModifier import ClassA
from AccessModifier import Base

class Product :
        def __init__(self):
                print('Object initialized')
        def __call__(self):
                print('Instance is called by special method')

if(__name__=='__main__'):
        ObjectofA = ClassA.A() 
        ObjectofA.funcPublic()
        #ObjectofA.__functionPrivate() # __functionPrivate s not known attribute
        ObjectofA.CallBothPublicAndPrivate()
        ObjectofA._A__functionPrivate() # # Calling the private member through name mangling

        ObjectBase = Base.Base()        
        ObjectBase.setClassName('Base A')
        print(ObjectBase.getClassName())
        print(ObjectBase.instanceVariableA)
        ObjectBase._Base__PrivateTester() # # Calling the private member through name mangling

        ProductObject = Product() 
        ProductObject()

        # testing lamda function
        lamdaTestAddThreeNumber = lambda a, b, c : a + b + c
        print(lamdaTestAddThreeNumber(1,2,3))

        #