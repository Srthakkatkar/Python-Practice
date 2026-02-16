numbers = [10, 20, 30, 40, 50]

position = int(input("Enter position: "))
value = int(input("Enter value to insert: "))

new_list = []

for i in range(len(numbers)):
    if i == position:
        new_list.append(value)
    new_list.append(numbers[i])

# Agar position last se baad ho
if position >= len(numbers):
    new_list.append(value)

print("Updated List:", new_list)

