# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]


def convert_in_single_list(input_list):

    output_list = []
    for i in input_list:
        if i not in output_list:
            output_list.append(i)

    return output_list


example_list = [1, 2, 3, 5, 1, 5, 3, 10] 

print(convert_in_single_list(example_list))