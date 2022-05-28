# Доп.задача 2
# 2. Есть такая вещь - палиндром. Это когда слово читается с обеих сторон одинаково. 
# Например, слово "шалаш". Также есть числовой палиндром. 
# Если при обратном чтении числа (124 - 421) не получается то же самое, то они складываются (124+421) и проверяются вновь. 
# Попробуйте написать функцию, находящую числовой палиндром.

import random

def search_palindrom():
    start_number = random.randint(10, 99999) 
    polindrom = 0
    
    while start_number != polindrom:
        start_number += polindrom
        temp = start_number
        polindrom = 0
        while temp != 0:
            polindrom = polindrom*10 + temp%10
            temp //=10

    print(f"polindrom = {polindrom}")


search_palindrom()