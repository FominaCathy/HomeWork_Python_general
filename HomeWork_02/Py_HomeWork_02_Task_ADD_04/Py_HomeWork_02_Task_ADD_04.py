#  Простые делители числа 13195 - это 5, 7, 13 и 29. 
#  Каков самый большой делитель числа 600851475143, являющийся простым числом?


def max_divider(number):
    div = 2 # первый простой делитель
    print(f"самый большой простой делитель числа {number} =", end=" ")
    while number != 1:
        if number % div == 0:
            number /= div
        else:
            div += 1

    print(f"{div}")


max_divider(600851475143)