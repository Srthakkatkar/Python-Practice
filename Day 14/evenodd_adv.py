"""
Program to check whether a number is Odd or Even
(Advanced Version)
"""

def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

try:
    a = int(input("Enter a number: "))
    result = check_odd_even(a)
    print(f"\n Yes The number {a} is {result}.")
except ValueError:
    print("\n No Invalid input! Please enter a valid integer.")
