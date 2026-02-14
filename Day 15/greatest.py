'''
    WRITE A PROGRAM TO FIND THE GREATEST NUMBER ENTERED BY USER USING LIST
'''

numbers = []   # empty list

# taking 3 inputs from user
for i in range(3):
    num = int(input(f"\n Enter number {i+1} : "))
    numbers.append(num)

# finding greatest number
greatest = max(numbers)

print("\n The Greatest Number is :", greatest)
