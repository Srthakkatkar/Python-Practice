numbers = [10, 20, 30, 20, 10, 50]

# Method 1: Using set()
remove_set = list(set(numbers))

# Method 2: Without changing order
remove_order = []

for num in numbers:
    if num not in remove_order:
        remove_order.append(num)

print("Original List :", numbers)
print("Using set() :", remove_set)
print("Without changing order :", remove_order)

