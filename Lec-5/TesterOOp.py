from AccessModifier import ClassA
from AccessModifier import Base

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
