a = int(input("Введите выручку фирмы: "))
b = int(input("Введите издержки фирмы: "))

if a < b:
    print ("Фирма работает в убыток")
elif a == b:
    print ("Прибыли нет")
elif a > b:
    print ("Фирма работает с прибылью")
    c = ((a - b)/a)*100
    print ("Рентабильность выручки: ", int(c))
    n = int(input("Введите количество сотрудников: "))
    d = (a-b)/n
    print ("Прибыль фирмы в расчете на одного сотрудника: ", int(d))