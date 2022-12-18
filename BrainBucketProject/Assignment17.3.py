numbers = []

def print_sum_avg(numbers):
    total = 0
    for i in numbers:
        total +=i
    average = total/len(numbers)
    print(total)
    print(average)

def add_num():
    for i in range(3):
        num = int(input("Enter number \n "))
        numbers.append(num)
    print_sum_avg(numbers)

add_num()



