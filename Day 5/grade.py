marks=int(input("Enter the marks of Student : "))

if(marks>=90 and marks<=100):
    print("\n The student got GRADE A ")
elif(marks>=90 and marks<=80):
    print("\n The student got GRADE B ")
elif(marks>=80 and marks<=35):
    print("\n The student got GRADE C")
elif(marks>=35 and marks<=0):
    print("\n The student got GRADE F")
else:
    print("\n Wrong information")  
