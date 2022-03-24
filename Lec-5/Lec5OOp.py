class Employee(object) :
    "Class to represent a employee class"
    def __init__(self, name, department, designation, age) -> None:
        self.m_name = name
        self.m_designation = designation
        self.m_department = department
        self.m_age = age
        
    def DisplayEmployeeInfo(self):
            print(f"Employee details {self.m_name}")

    def PublicApi():
        print('I am a public API')
    
    def _PrivateApi():
        print('I am a private API')

e1 = Employee('mhas', 'mis', 'se', 35)
e1.DisplayEmployeeInfo()
#print(e1.orphanItem)
