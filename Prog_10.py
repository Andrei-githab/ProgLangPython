import datetime


class Loger:

    def __init__(self):
        pass

    def Start(self, message):
        print("Начало сеанса:" + message)

    def Coordinates(self):
        print("Coordinates:")

    def CoordiChangedCircle(self, x, y):
        print("Координаты изменены / окружность / " + "x = " + x + " y = " + y)


now = datetime.datetime.now()
log = Loger()
log.Start(now.strftime("%d-%m-%Y %H:%M"))
log.Coordinates()
log.CoordiChangedCircle("4", "6")
