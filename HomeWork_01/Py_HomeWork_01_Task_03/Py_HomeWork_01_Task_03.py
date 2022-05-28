# Задача 3
# Подсчитать сумму цифр в вещественном числе.

def sumNumbers(number):
    summ = 0 
    i = 0
    for i in str(number):
        if i != '.':
            summ += int(i) 
    print(f'сумма цифр числа {number} = {summ}')

sumNumbers(123.56)
