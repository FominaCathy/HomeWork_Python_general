# Задача 4
# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def rowMultiply(number):
    row = []
    i = 1
    temp = 1
    for i in range(1,number+1):
        temp *= i
        row.append(temp)
    print(row)

rowMultiply(4)