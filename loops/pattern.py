num = int(input("enter your number"))

for i in range(1,num+1):
    for j in range(0,i):
        print("*", end ="")
    print()
    


for i in range(1,num+1):
    for j in range(0,i):
        print(j, end ="")
    print()



for i in range(1,num+1):
    for j in range(0,i):
        print(i, end ="")
    print()


for i in range(1,num+1):
    for j in range(0,i):
        print(j+1, end ="")
    print()

for i in range(num, 1):
    for j in range(i,0):
        print("*",end="")
    print()
    