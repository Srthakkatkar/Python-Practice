import copy

student_info = ["Atharv", 96, ["O"]]

print("\nOriginal List :", student_info)

# Shallow Copy
shallow_copy = copy.copy(student_info)

# Deep Copy
deep_copy = copy.deepcopy(student_info)

index = int(input("\nEnter index to change (grade list index = 2): "))
value = input("Enter new value : ")

# Changing nested list
shallow_copy[index][0] = value
deep_copy[index][0] = value

print("\n After Modification ")

print("\nOriginal List :", student_info)
print("Shallow Copy  :", shallow_copy)
print("Deep Copy     :", deep_copy)

