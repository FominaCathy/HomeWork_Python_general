
# Задача:
# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


def exponential_Row(number): 
    i = 0
    while i < number:
        print(((-3)**i), end=' ')
        i += 1

exponential_Row(5)