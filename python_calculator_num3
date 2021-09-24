import math


class Calculator:
    def __init__(self):
        self.command = ""
        self.result = 0
        self.degree = 0
    def calc_read(self):
        print("Введите номер команды от 1 до 3 (1 - sin, 2 - cos, 3 - tan, 4 - ctg) ")
        self.command = int(input())
        print("Введите угол в градусах: ")
        self.degree = int(input())
    def calc_print(self):
        print("Ответ: ")
        print(round(self.result, 2))
    def calc_degrees(self):
        rad = (self.degree * math.pi) / 180
        if self.command == 1:
            self.result = math.sin(rad)
        elif self.command == 2:
            self.result = math.cos(rad)
        elif self.command == 3:
            self.result = math.tan(rad)
        elif self.command == 4:
            self.result = math.cos(rad) / math.sin(rad)
        else:
            pass

calca = Calculator()
calca.calc_read()
calca.calc_degrees()
calca.calc_print()
