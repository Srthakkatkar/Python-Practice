student_info = [56, 36, 96]

# 1. Normal reverse (in-place)
rev1 = student_info.copy()
rev1.reverse()

# 2. Reverse using slicing (new list)
rev2 = student_info[::-1]

# 3. Reverse using loop (logic-based)
rev3 = []
for i in range(len(student_info) - 1, -1, -1):
    rev3.append(student_info[i])

# 4. Reverse using reversed() iterator
rev4 = list(reversed(student_info))

# Output
print("Original List :", student_info)
print("Reverse()     :", rev1)
print("Slicing       :", rev2)
print("Loop Reverse  :", rev3)
print("reversed()    :", rev4)
