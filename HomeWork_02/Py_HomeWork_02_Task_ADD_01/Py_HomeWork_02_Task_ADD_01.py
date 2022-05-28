#  Написать программу преобразования двоичного числа в десятичное.


def conversion_decimal(num_binary):

    num_decimal = 0
    max_degree = len(num_binary) - 1

    for i in num_binary:
        num_decimal += int(i)*(2 ** max_degree)
        max_degree -= 1

    return num_decimal

number_binary = 10001000 #36
print(f"десятичное представление числа {number_binary} = {conversion_decimal(str(number_binary))}")

number_binary = 1011 #11
print(f"десятичное представление числа {number_binary} = {conversion_decimal(str(number_binary))}")
