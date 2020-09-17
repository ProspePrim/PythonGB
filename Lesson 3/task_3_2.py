#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. 
# Реализовать вывод данных о пользователе одной строкой

def par_func(name, surname, by, city, email, phone):
    print(name, surname, by, city, email, phone)

par_func(name= 'Vasya', surname='Ivanov', by=1905, city='Moscow', email='email', phone='666') 