#Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.

#Подсказка: использовать функцию count() и cycle() модуля itertools. 
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from itertools import count

from itertools import cycle

def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el >= stop_number:
            break
        else:
            print(el)
def my_cycle_func(my_list, iteration):
    i = 1
    iter = cycle(my_list)
    while i <= iteration:
        print(next(iter))
        i+=1

my_count_func(start_number = int(input("Введите первое число: ")), stop_number = int(input("Введите последнее: ")))
my_cycle_func(my_list = ['a', 'b', 'c', '2', '3', '5'], iteration = int(input("Введите количество итераций: "))) 