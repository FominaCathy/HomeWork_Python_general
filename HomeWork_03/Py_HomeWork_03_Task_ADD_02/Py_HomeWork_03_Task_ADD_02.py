# Определите функцию, которая удаляет весь текст, следующий за любым из переданных маркеров комментариев. Любые пробелы в конце строки также должны быть удалены.
# Пример: 
# Входные данные:
# «apples, pears # and bananas
# grapes
# bananas !apples          » 
# Выходные данные:
# «apples, pears
# grapes
# bananas»
# Функция может вызываться вот так:
# result = function("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

def function_delete(input_text, symbol_list: list):
    
    split_text = input_text.split("\n")
    len_split_text = len(split_text)
    for i in range(0, len_split_text):
        for s in symbol_list:
            if split_text[i].find(s) != -1:
                split_text[i]  = split_text[i].replace(split_text[i][split_text[i].find(s):], "")
                
    output_text = "\n".join(split_text) 
    
    return output_text



result = function_delete("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

print(result)