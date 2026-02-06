# def palindrom(num):
#     rev  = 0
#     while num>0:
#         digit = num % 10
#         rev =rev*10 + digit
#         num = num//10
#     return rev
# num = int(input("Enter your number"))
# palindrom_num = palindrom(num)
# print(palindrom_num)


def is_palindrom(text):
    text = text.lower()
    rev =""
    for char in text:
        rev = char+rev
    if text == rev:
        return True
    else:
        return False
text =input("Enter your number")
palindrom = is_palindrom(text)
print(palindrom)