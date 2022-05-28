# Написать программу преобразования десятичного числа в двоичное


def conversion_binary(num_decimal):
    num_binary = ""

    while num_decimal > 1 :
        num_binary = str(num_decimal%2) + num_binary 
        num_decimal //= 2

    return str(num_decimal) + num_binary 
    

number_decimal = 136
print(f"двоичное представление числа {number_decimal} - {conversion_binary(number_decimal)}")
