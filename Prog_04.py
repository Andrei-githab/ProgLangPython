"""
Лабораторная работа 4
Считать с файла текст, вывести в выходной файл
1) длину файла
2) количество гласных
3) самую часто употребляемую букву
4) количество строчек
"""


def getKolGlas(text):
    text = text.lower()
    countglas = 0
    for glas in 'aeiouyауоыиэяюёе':
        countglas += text.count(glas)
    return countglas


def getLetterCountFrequency(message):
    message = message.upper()
    message = message.replace(" ", "")
    charmasiv = {}
    for letter in message:
        try:
            charmasiv[letter] += 1
        except:
            charmasiv[letter] = 1
    letCountFreq = sorted(charmasiv.items(), key=lambda mc: mc[1], reverse=True)
    charCountFreq = letCountFreq[0]
    return charCountFreq[0]


print("############ Работа с файлом ############\n")
dataFile = open("input_04.txt", "r", encoding="utf-8")
data = dataFile.read()
lenInput = str(len(data))
kolGlas = str(getKolGlas(data))
letterCountFrequency = str(getLetterCountFrequency(data))
kolLines = str(len(open("input_04.txt").readlines()))
dataFile.close()
infoData = open("output_04.txt", "w", encoding="utf-8")
infoStr = "Что в файле: \n\nДлина файла: " + lenInput + "\nКоличесчтво глассных: " + kolGlas + "\nЧасто употребляемая буква: " + letterCountFrequency + "\nКоличество строчек: " + kolLines
infoData.write(infoStr)
print(infoStr)
infoData.close()
