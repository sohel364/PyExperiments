class Employee(object) :
    "Class to represent a employee class"
    def __init__(self, name, department, designation, age) -> None:
        self.m_name = name
        self.m_designation = designation
        self.m_department = department
        self.m_age = age

    def DisplayEmployeeInfo(self):
        self.orphanItem = 10
        if self.age > 35 :
            print("Employee details", self.name, self.designation, self.department, self.age)
        else :
            print("There was no one above 35 !")


e1 = Employee('mhas', 'mis', 'se', 35)
e1.DisplayEmployeeInfo()
print(e1.orphanItem)
