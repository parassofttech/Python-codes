def count_vowels(text):
    count = 0
    text = text.lower()
    for char in text:
        if char in 'aeiou':
            count +=1
    return count
text = input("Enter your word")  
string = count_vowels(text)
print(string)