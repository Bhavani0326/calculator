print("select option")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

a=int(input())
b=int(input())

choice=int(input(("Enter choice 1/2/3/4:")))

if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a-b)
elif choice==4:
    print(a/b) if b!=0 else "undefined"
else:
    print("invalid input")
