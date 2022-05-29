# Найти НОК двух чисел


def simple_divisors(number): # функция разложения на простые множители
    simple_div = {}

    i= 2
    while number != 1:
        if number % i == 0:
            if i in simple_div:
                simple_div[i] = simple_div.get(i) + 1
            else:
                simple_div[i] =  1
            number /= i
        else:
            i += 1

    return simple_div



def search_nok(number_first, number_second):
    nok = 1
    # разложим на простые множители оба числа

    simple_div_first = simple_divisors(number_first)
    simple_div_second = simple_divisors(number_second)

    for i in simple_div_first:
        if i in simple_div_second:
            nok *= i ** max(simple_div_first.get(i), simple_div_second.pop(i))
        else:
            nok *= i ** simple_div_first.get(i)
    
    for i in simple_div_second:
        nok *= i ** simple_div_second.get(i)

    return nok


print(f"НОК чисел 12 и 48 = {search_nok (12, 48)}")

print(f"НОК чисел 130 и 15 = {search_nok(130, 15)}")