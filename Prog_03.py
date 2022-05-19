"""
Лабораторная работа 3 
Считываем с консоли строку выводим наибольшую подстроку
между символами *, её длину, выводим заборчиком (То ЕсТь ВоТ тАк)
"""


def remove_str(str):
    result = str[1: -1]
    return result


print("########## Программа Забор ##########")
stroka = input("Введите строку: ")
newstroka = stroka.split('*')
strokadel = remove_str(newstroka)
maxpodstr = max(strokadel, key=len)
obrstr = ""
for i in range(len(maxpodstr)):
    if i % 2 == 0:
        obrstr += maxpodstr[i].upper()
    else:
        obrstr += maxpodstr[i].lower()
print("Обработанная строка: ", obrstr)
print("Длина строки: ", len(obrstr))
