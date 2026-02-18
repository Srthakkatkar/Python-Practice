str1 = "Leo Messi"
ch = input("Enter character to find: ")

index = str1.find(ch)

while index != -1:
    print("Found at index:", index)
    index = str1.find(ch, index + 1)



