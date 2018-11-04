x = int(input("Enter The Height : "))
y = int(x)
for i in range(0, x):
    for j in range(0,y):
        print(" ",end="")
    y -= 1
    for k in range(0,i+1):
        print("*",end=" ")
    if(i!=x-1):
        print("")
