def palindrom(num):
    rev  = 0
    while num>0:
        digit = num % 10
        rev =rev*10 + digit
        num = num//10
    return rev
num = int(input("Enter your number"))
palindrom_num = palindrom(num)
print(palindrom_num)