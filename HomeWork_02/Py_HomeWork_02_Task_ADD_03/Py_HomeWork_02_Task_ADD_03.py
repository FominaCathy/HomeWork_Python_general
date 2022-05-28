# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. 
# Начиная с 1 и 2, первые 10 элементов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

def summ_elemetn_fibonachi ():
    element_f_prev = 1 # 1й элемент
    element_f_next = 2 # 2й элемент
    i = 0
    row_fibonachi = [1,2]

    while (row_fibonachi[i]+row_fibonachi[i+1]) <= 4000000:
        row_fibonachi.append(row_fibonachi[i]+row_fibonachi[i+1])
        i += 1

    print(f"ряд Фибоначчи: {row_fibonachi}")

    summ_element = 0    
    for i in range(1, len(row_fibonachi),2):
        summ_element += row_fibonachi[i]
    
    return summ_element

print(f"сумма четных элементов ряда Фибоначчи = {summ_elemetn_fibonachi ()}")

