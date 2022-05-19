"""
Лабораторная работа 7
Написать программу реализующию словарь(англ===>рус)
В базе должно быть 10 заранее слов
Функционал(через функции)
    1)добавить пару
    2)удалить
    3)проверить есть ли уже в базе
    4)вывести слова на англ короче 5 символов
    5)очистить словарь
    6)отсортировать словарь
    7)вывести весь словарь
    8)изменить пару
    9)поменять ключ и значение местам
"""


def getPrintDictionary(pdictionary):
    for key, value in pdictionary.items():
        print("{0}: {1}".format(key, value), end=" ")
    return ""


def getNewElementDictionary(nedictionary):
    print("Добавить элемент")
    newkey = input("Введите ключ: ")
    newvalue = input("Введите значение: ")
    nedictionary[newkey] = newvalue
    return getPrintDictionary(nedictionary)


def getDellElementDictionary(delldictionary):
    print("Добавить элемент")
    dellkey = input("Введите ключ: ")
    del delldictionary[dellkey]
    return getPrintDictionary(delldictionary)


def getProvercaPar(pardictionary):
    print("Проверки наличия пары\nВведите пару")
    kayp = input("Ключ: ")
    valp = input("Значение: ")
    if (kayp, valp) in pardictionary.items():
        print("Есть такая пара")
    else:
        print("Нет такой пары")


def getMinFElemetDictionary(minfelemen):
    print("Вывод слов на английском короче 5 символов")
    for key, value in minfelemen.items():
        if len(key) < 5:
            print("{0}: {1}".format(key, value))
    return ""


def getClearDictionary(cdictionary):
    cdictionary.clear()
    print("Словарь очищен")
    return getPrintDictionary(cdictionary)


def getSortDictionary(sdictionary):
    print("Отсортированный словарь")
    list_keys = list(sdictionary.keys())
    list_keys.sort()
    for i in list_keys:
        print(i, ':', sdictionary[i])
    return 0


def getChangeDictionary(chdictionary):
    print("Изменить пару\nВведите пару")
    kayc = input("Старый Ключ: ")
    nkayc = input("Новый ключ: ")
    valc = input("Значение: ")
    chdictionary[nkayc] = chdictionary[kayc]
    del chdictionary[kayc]
    chdictionary[nkayc] = valc
    return getPrintDictionary(chdictionary)


def getInverseDictionary(idictionary):
    print("Инвертированы словарь")
    inverse_dictionary = {}
    for kayDic, volDic in idictionary.items():
        inverse_dictionary[volDic] = kayDic
    return getPrintDictionary(inverse_dictionary)


slovDictionary = {"cat": "кот",
                  "russian": "русский",
                  "college": "колледж",
                  "home": "дом",
                  "language": "язык",
                  "base": "база",
                  "telecommunications": "телекоммуникации",
                  "data": "данные",
                  "chorus": "хор",
                  "hall": "хол",
                  "bread": "хлеб"}

print("############ Работа со словарём ############\n")
running = True
while running:
    try:
        commonda = int(
            input("\n\nЧто можно сделать\n 1 - добавить пару \n 2 - удалить пару \n 3 - проверить есть ли уже в базе \n "
              "4 - вывести слова на англ короче 5 символов \n 5 - очистить словарь \n 6 - отсортировать словарь \n "
              "7 - вывести весь словарь \n 8 - изменить пару \n 9 - поменять ключ и значение местам \n 0 - выход"
              "\n\nВведите цифру того что хотите сделать > "))
    except ValueError:
        print('Введите число!')
    else:
        if commonda == 1:
            getNewElementDictionary(slovDictionary)
        elif commonda == 2:
            getDellElementDictionary(slovDictionary)
        elif commonda == 3:
            getProvercaPar(slovDictionary)
        elif commonda == 4:
            getMinFElemetDictionary(slovDictionary)
        elif commonda == 5:
            getClearDictionary(slovDictionary)
        elif commonda == 6:
            getSortDictionary(slovDictionary)
        elif commonda == 7:
            getPrintDictionary(slovDictionary)
        elif commonda == 8:
            getChangeDictionary(slovDictionary)
        elif commonda == 9:
            getInverseDictionary(slovDictionary)
        elif commonda == 0:
            break
        else:
            print("Hет такой команды")
