'''
    WRITE A PROGRAM TO FIND THE GRETEST NUMBER ENTERED BY USER 
'''

a=int(input("\n Enter the number a :  "))
b=int(input("\n Enter the number b :  "))
c=int(input("\n Enter the number c :  "))


if a>b and a>c:
        print("\n The Number ",a,"is greatest")

elif b>a and b>c:
        print("\n The Number ",b,"is greatest")

else:
        print("\n The Number ",c,"is greatest")
