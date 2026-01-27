student_info=[90,90,87,67]

print("\n Lenght of lst : ",len(student_info))
a=int(input("\n Enter the index do you want to store : "))
data=input("\n enter the data : ")
student_info.insert(a,data)
print(student_info)

list.remove(90)
print(student_info)