class Employee(object) :
    def __init__(self, name, department, designation, age) -> None:
        self.name = name
        self.designation = designation
        self.department = department
        self.age = age
        self._salary = 10000
                
    def DisplayEmployeeInfo(self):
        self.orphanItem = 10
        if self.age > 35 :
            print("Employee details", self.name, self.designation, self.department, self.age)
        else :
            print("There was no one above 35 !")
    

    def PublicApi():
        print('I am a public API')
    
    def _PrivateApi():
        print('I am a private API')

e1 = Employee('mhas', 'mis', 'se', 35)
e1.DisplayEmployeeInfo()
print(e1.orphanItem)
