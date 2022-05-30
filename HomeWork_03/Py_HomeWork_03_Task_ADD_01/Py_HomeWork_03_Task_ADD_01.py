# Определите функцию, которая принимает римскую цифру в качестве аргумента 
# и возвращает ее значение в виде числового десятичного целого числа. 
# Вам не нужно проверять форму римской цифры. 
# Современные римские цифры записываются путем выражения каждой десятичной цифры числа, 
# которое должно быть закодировано отдельно, начиная с самой левой цифры. 
# Таким образом, 1990 отображается "MCMXC" (1000 = M, 900 = CM, 90 = XC), 
# а 2008 отображается "MMVIII" (2000 = MM, 8 = VIII). 
# Римская цифра для 1666, "MDCLXVI", использует каждую букву в порядке убывания. 
# Пример: имя_вашей_функции ('XXI') # должно вернуть 21




def tranclit_roman_in_arab(roman_number):
    # создадим словарь
    roman_dict = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D" : 500, "M" : 1000}

    len_roman = len(roman_number)

    arab_number = roman_dict[roman_number[-1]]
    for i in range(-2, -len_roman-1, -1):
        if roman_dict[roman_number[i]] >= roman_dict[roman_number[i+1]]:
            arab_number += roman_dict[roman_number[i]]
        else:
            arab_number -= roman_dict[roman_number[i]]

    return arab_number


roman_num = "MCMXC" 
print(f"{roman_num} = {tranclit_roman_in_arab(roman_num)}")

roman_num = "XXI" 
print(f"{roman_num} = {tranclit_roman_in_arab(roman_num)}")

roman_num = "MMVIII"
print(f"{roman_num} = {tranclit_roman_in_arab(roman_num)}")
