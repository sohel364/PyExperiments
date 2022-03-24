class Employee(object) :
    "Class to represent a employee class"
    def __init__(self, name, department, designation, age) -> None:
        self.m_name = name
        self.m_designation = designation
        self.m_department = department
        self.m_age = age

    def DisplayEmployeeInfo(self):
            print(f"Employee details {self.m_name}")



e1 = Employee('mhas', 'mis', 'se', 35)
e1.DisplayEmployeeInfo()
#print(e1.orphanItem)
