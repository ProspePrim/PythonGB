#Необходимо создать (не программно) текстовый файл, 
#где каждая строка описывает учебный предмет и наличие лекционных, 
#практических и лабораторных занятий по этому предмету и их количество. 
#Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
#Вывести словарь на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import json

subj = {}
with open('file_5_5.txt', 'r') as init_f:
    for line in init_f:
        a = line.replace("-",'')
        b = a.split()
        the_sum = 0
        i = 1
        for i in range(1,len(b)):
            the_sum += int(b[i])
        #print(the_sum)
        subj[b[0]] = the_sum  
    print(f'Общее количество часов по предмету :\n {subj}' , sep = "\n")
    



    