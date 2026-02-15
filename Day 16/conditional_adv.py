a = 40
b = 20
c = 40

if a == b:
    print("a and b are equal")

    if a == c:
        print("a, b and c are equal")
    else:
        print("a and b are equal but not equal to c")

else:
    print("a and b are not equal")

    if a == c:
        print("But a and c are equal")
    else:
        print("None of them are equal")
