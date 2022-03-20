import math

class Calculator:
    def __init__(self):
        self.result = 0
        self.degree = 0
        self.commands = {
            "sin" : self.sin_solver(),
            "cos" : self.cos_solver(),
            "tan" : self.tan_solver(),
        }

    def calc_read(self):
        self.degree = int(input("Введите угол в градусах: "))
        command = input("Введите функцию: ")
        self.commands[command]

    def calc_print(self):
        print(f"Ответ: {round(self.result, 2)}")

    def sin_solver(self):
        rad = (self.degree * math.pi) / 180
        self.result = math.sin(rad)

    def cos_solver(self):
        rad = (self.degree * math.pi) / 180
        self.result = math.cos(rad)

    def tan_solver(self):
        rad = (self.degree * math.pi) / 180
        self.result = math.tan(rad)


calc = Calculator()
calc.calc_read()
calc.calc_print()
