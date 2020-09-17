#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов

a = int(input("Ведите a: "))
b = int(input("Ведите b: "))
c = int(input("Ведите c: "))

def sum_func(x, y, z):
    list_a = [x, y, z]
    list_a.sort()
    list_b = [list_a[1], list_a[2]]
    print(sum(list_b))
sum_func(a, b, c)