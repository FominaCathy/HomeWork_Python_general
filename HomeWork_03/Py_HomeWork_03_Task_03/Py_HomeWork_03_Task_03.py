# Составить список простых множителей натурального числа N


def simple_divisors(number): # функция разложения на простые множители
    simple_div = []

    i= 2
    while number != 1:
        if number % i == 0:
            simple_div.append(i)
            number /= i
        else:
            i += 1

    return simple_div

print(simple_divisors(125))