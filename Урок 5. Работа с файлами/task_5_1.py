#Создать программно файл в текстовом формате, записать
#в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.



with open('test.txt', 'w') as my_f:
    line = input('Введите текст \n')
    while line:
        my_f.writelines(line + ' \n' )
        line = input('Введите текст \n')
        if not line:
            break
        
    
with open('test.txt', 'r') as my_f:
    print(my_f.read())


# Хотел сделать так, что бы было возможно выводить содержание 
# не открывая файл повторно, но ничего не получилось.
# Есть идеи?

