a = int(input("Введите число"))

b = a//3600
c = (a%3600)//60
d = (a%60)

print ("Вы ввели:{}".format(a))
print ("Ответ: {}:{}:{}".format(b,c,d))
