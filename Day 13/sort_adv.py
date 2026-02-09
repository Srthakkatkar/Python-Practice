# Student information list
student_info = [300, 45, 56, 102, 89]

# 1. Normal ascending sort
asc = sorted(student_info)

# 2. Normal descending sort
desc = sorted(student_info, reverse=True)

# 3. Sort by number of digits
digit_sort = sorted(student_info, key=lambda x: len(str(x)))

# 4. Sort by last digit
last_digit_sort = sorted(student_info, key=lambda x: x % 10)

# 5. Advanced: sort by digits first, then by value
advanced_sort = sorted(student_info, key=lambda x: (len(str(x)), x))

# Output
print("Original List      :", student_info)
print("Ascending          :", asc)
print("Descending         :", desc)
print("By Digit Count     :", digit_sort)
print("By Last Digit      :", last_digit_sort)
print("Advanced Sort      :", advanced_sort)
