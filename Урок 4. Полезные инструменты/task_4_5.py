#Реализовать формирование списка, используя функцию range() и возможности генератора. 
#В список должны войти четные числа от 100 до 1000 (включая границы). 
#Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().

from functools import reduce

my_new_list = [el for el in range(100,1001) if el % 2 == 0]
sum_all = reduce(lambda x,y: x + y, my_new_list)
print(sum_all)


p_all = reduce(lambda x,y: x * y, my_new_list)
print(p_all)