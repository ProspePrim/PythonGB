#Создать текстовый файл (не программно), сохранить в нем несколько строк, 
#выполнить подсчет количества строк, количества слов в каждой строке.

with open('test.txt', 'w') as my_f:
    my_l = []
    line = input('Введите текст \n')
    while line:
        my_l.append(line + '\n')
        
        line = input('Введите текст \n')
        if not line:
            break
    
    my_f.writelines(my_l)

with open('test.txt' , 'r') as f:
    i = 0
    for el in f:
        i += 1
        print(f"Строка {i}: {el}")
        
        count = len(el) - el.count("\n")
        print(f"Количество знаков: {count}")

        print(f"Количество слов в строке: {len(el.split())} ")
        print('_____________________________________')
    print('*'*20)    
    print(f"Количество строк: {i}")
