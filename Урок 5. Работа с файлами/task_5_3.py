#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов 
#(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., 
#вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
from functools import reduce

with open('salary_1.txt','r') as sal_t:
    sal = []
    poor = []
    for el in sal_t:
        sal_a = el.split()
        if float(sal_a[1]) < 20000:
            poor.append(sal_a[0])
        sal.append(sal_a[1])
    

print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')



