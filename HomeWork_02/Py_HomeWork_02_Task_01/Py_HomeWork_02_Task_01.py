
# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4



def summ_odd_position(array):
    summ = 0
    len_array = len(array)
    for i in range(0,len_array,2):
        summ += array[i]

    print(f"сумма нечетных позиций = {summ}")
 
arr = [1,2,3,4,5,78,2]

summ_odd_position(arr)