# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def multiply_pair(array):

    mult_array = []
    len_array = len(array)-1
    i = 0

    while i <= len_array - i:
        mult_array.append(array[i] * array[len_array-i])
        i += 1

    print(mult_array)


arr = [2, 3, 4, 5, 6]
multiply_pair(arr)

arr = [2, 3, 5, 6] 
multiply_pair(arr)