# Задача № 2
# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def NumberRepet (baseStr, searchStr):
    lengthSearchStr = len(searchStr) # длина строки которую ищем
    lengthBaseStr = len(baseStr)
    i = 0
    count = 0 # счетчик для вхождений
    while i < lengthBaseStr-lengthSearchStr+1:
        if baseStr[i:i+lengthSearchStr] == searchStr:
            count += 1
        i += 1
    print(f"кол-во вхождений подстроки в основную строку = {count}")

firstStr = 'lalamymy lal mimituttu'
secondStr = 'tu'

NumberRepet(firstStr, secondStr)