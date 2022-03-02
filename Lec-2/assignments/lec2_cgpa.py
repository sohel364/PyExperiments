#Calculate CGPA from achived percentage
print("Program to check CGPA from achived percentage. ")
percentage = input('Achieved percentage in exam : ')
value = int(percentage)

if value < 40 :
    print(str(value) + "% = Grade : F")

elif value >= 40 and value < 50 :
    print(str(value) + "% = Grade : E")

elif value >= 50 and value < 60 :
    print(str(value) + "% = Grade : D")

elif value >= 60 and value < 70 :
    print(str(value) + "% = Grade : C")

elif value >= 70 and value < 80 :
    print(str(value) + "% = Grade : B")

elif value >= 80 and value < 90 :
    print(str(value) + "% = Grade : A")    

elif value >= 90 and value < 100 :
    print(str(value) + "% = Grade : A")                