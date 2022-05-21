import datetime

class Loger:
    global now
    naw = datetime.datetime.now()
    def startl(self):
        print("<Запуск программы>[{}]/[{}]/[{}]/[{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute))
        
    def X_peremeshchenie(self):
        print("<Запуск программы>[{}]/[{}]/[{}]/[{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute))


startloger = Loger()
startloger.startl()
