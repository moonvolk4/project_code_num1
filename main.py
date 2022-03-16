import numpy as np
status = True
while status == True:
    a = float(input("Введите начало интервала:"))
    b = float(input("Введите конец интервала:"))
    f = input("Введите уравнение:")
    f1 = eval(f.replace("x", "a"))
    f2 = eval(f.replace("x", "b"))
    print(f"Левый конец отрезка: {f1}")
    print(f"Правый конец отрезка: {f2}")
    print("Проверка...")
    if f1 < 0 and f2 > 0:
        print(f"x e [{a};{b}]")
    else:
        print(f"x !e [{a};{b}]")
        status = False
    arr = []
    for i in np.arange(a, b, 0.1):
        arr.append(round(i, 2))
    answer = {}
    for el in range(len(arr)):
        x = arr[el]
        answer[x] = abs((x**3)-5*x+3)

    print(min(answer, key=answer.get))
