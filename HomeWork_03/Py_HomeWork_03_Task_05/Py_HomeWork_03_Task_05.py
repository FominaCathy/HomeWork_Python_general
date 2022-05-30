#5.  Дан текстовый файл, содержащий целые числа. 
# Удалить из него все четные числа. 

import random

def print_file(name_file): # печать данных файла

    with open(name_file, 'r') as data_f:
        for line in data_f:
            print(line, end="")



data_file = open('file.txt', 'w') # заполнили файл случайными числами
for i in range(10):
    temp = str(random.randint(1, 101))
    data_file.write(temp + '\n')

data_file.close() # закрыли файл

print("печать начального  файла")
print_file('file.txt')


number_list = []

with open('file.txt', 'r') as data_f:
    for line in data_f:
        if int(line)%2 != 0:
            number_list.append(line)


data_file = open('file.txt', 'w')
data_file.writelines(number_list) # записали в файл новые данные
data_file.close() # закрыли файл

print("печать измененного файла")
print_file('file.txt')