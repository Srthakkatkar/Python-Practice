marks = int(input("Enter the marks of Student : "))

# Validation
if marks < 0 or marks > 100:
    print("\nWrong information")

# Grade Calculation
elif marks >= 90:
    print("\nThe student got GRADE A")

elif marks >= 80:
    print("\nThe student got GRADE B")

elif marks >= 35:
    print("\nThe student got GRADE C")

else:
    print("\nThe student got GRADE F")
