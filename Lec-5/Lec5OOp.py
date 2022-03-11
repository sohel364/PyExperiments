class Employee(object) :
    def __init__(self, name, department, designation, age) -> None:
        self.name = name
        self.designation = designation
        self.department = department
        self.age = age

    def DisplayEmployeeInfo(self):
        self.orphanItem = 10
        if self.age > 35 :
            print("Employee details", self.name, self.designation, self.department, self.age)
        else :
            print("There was no one above 35 !")


e1 = Employee('mhas', 'mis', 'se', 35)
e1.DisplayEmployeeInfo()
print(e1.orphanItem)
