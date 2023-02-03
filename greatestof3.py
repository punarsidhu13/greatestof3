a = int(input("Enter First Number:-\n "))
b = int(input("Enter Second Number:-\n "))
c = int(input("Enter Third Number:-\n "))

if a>b:
    if a>c:
        print("A is Greatest of the 3 Numbers")
    else:
        print("C is Greatest of the 3 Numbers") 
elif b>c:
    print("B is Greatest of the 3 Numbers")
else:
    print("C is Greatest of the 3 Numbers")
