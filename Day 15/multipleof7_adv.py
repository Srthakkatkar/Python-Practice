'''
    Write a program to check whether the number entered by user 
    is within range (1 to 100) and multiple of 7 or not
'''

a = int(input("\n Enter the number : "))

# Range Check
if 1 <= a <= 100:
    print("\n Number is within range (1 - 100)")

    # Multiple of 7 Check
    if a % 7 == 0:
        print(" The number", a, "is a Multiple of 7")
    else:
        print(" The number", a, "is NOT a Multiple of 7")

else:
    print("\n Number is OUT of range (1 - 100)")
