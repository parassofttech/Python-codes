def num_avg(numbers):
    total =0
    for num in numbers:
        total+=num 
        avg = total/5
        return avg
average = num_avg([2,7,4,3,8])
print(average)