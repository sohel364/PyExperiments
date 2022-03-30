class Base :
    className = '' # a class variable

    def setClassName(self, name):
        self.className = name
        self.instanceVariableA = 'variable A'

    def getClassName(self):
        self.instanceVariableA +=' The Getter is talking'
        return self.instanceVariableA

    def __PrivateTester(self):
        print('Private function i called')