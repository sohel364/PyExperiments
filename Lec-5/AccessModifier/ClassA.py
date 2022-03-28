class A :
    def funcPublic(self):
        print('this is public function')
    def __functionPrivate(self):
        print('this is private')

    def CallBothPublicAndPrivate(self):
        self.funcPublic()
        self.__functionPrivate()