import json
from unicodedata import name

class Person :
    def __init__(self, name, age, address) :
        self.name = name
        self.age = age
        self.address = address

    def ShowPersonDetails(self) :
        print(self.name + self.age + self.address)

x = '{"name" : "Simon","age":30, "address" : "23 rockstreen"}'
y = json.loads(x) #parse x

PersonObject = Person(y["name"], y["age"], y["address"])

print(PersonObject.ShowPersonDetails)