#Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. 
# Выполните вызов методов и также покажите результат.

class Coffee:
    def __init__(self, title):
        self.title = title



class black_coffee(Coffee):
    def __init__(self, title):
        super().__init__(title)

    def drink(self):
        return f'Вы пьёте: {self.title}'

class Tea:
    def __init__(self, title):
        self.title = title


class milk_tea(Tea):
    def __init__(self, title):
        super().__init__(title)

    def drink(self):
        return f'Вы пьёте: {self.title}'



Americano = black_coffee("Американо")
Ulun = milk_tea("Улун")

print(Americano.drink())

print(Ulun.drink())