#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
#В расчете необходимо использовать формулу:  (выработка в часах*ставка в час) + премия.
#Для выполнения расчета для конкретных значений необходимо  запускать скрипт с параметрами.

import sys

name, time, salary, benefits = sys.argv

try:
    time = int(time)
    salary = int(salary)
    benefits = int(benefits)
    res = (time * salary) + benefits
    print(f'Заработная плата сотрудника  {res}')

except ValueError:
    print('Invalid args')