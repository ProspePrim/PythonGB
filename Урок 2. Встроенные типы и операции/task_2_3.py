#Пользователь вводит месяц в виде целого числа от 1 до 12. 
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
#Напишите решения через list и через dict.


s_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
s_list = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input("Введите номер месяца: "))
if month ==12 or month == 1 or month == 2:
        print(s_dict.get(1))
        print(s_list[0])
elif month == 3 or month == 4 or month ==5:
    print(s_dict.get(2))
    print(s_list[1])
elif month == 6 or month == 7 or month == 8:
    print(s_dict.get(3))
    print(s_list[2])

elif month == 9 or month == 10 or month == 11:
    print(s_dict.get(4))
    print(s_list[3])
else:
        print("Ошибка, введите корректное значение") 