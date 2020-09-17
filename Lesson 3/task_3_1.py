#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

def func_div (a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "Число b не может быть равно 0"
    except ValueError:
        return "Введите число"
print(func_div(a, b))