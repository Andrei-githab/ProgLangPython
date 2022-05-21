import datetime


class Loger:
    def __init__(self, x):
        self.x = x

    def startl(self):
        now = datetime.datetime.now()
        print("<Запуск программы>[{}]/[{}]/[{}]/[{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute))

    def X_peremeshchenie(self):
        now = datetime.datetime.now()
        print("<Запуск программы>[{}]/[{}]/[{}]/[{}:{}]".format(now.day, now.month, now.year, now.hour, now.minute))
        return


startloger = Loger()
startloger.startl()
startloger.X_peremeshchenie()
