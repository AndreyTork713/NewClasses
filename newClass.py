

class NewClass(object):
    def __init__(self, name='no name', age=10, id=123456):
        self.name = name
        self.age = age
        self.id = id

    def say_name(self):
        return f'Моё имя: {self.name}'

    def say_age(self):
        if self.age % 10 == 1:
            pref = 'год'
        elif self.age % 10 >= 5 or self.age % 10 == 0:
            pref = 'лет'
        else:
            pref = 'года'
        return f'Мой возраст: {self.age} {pref}'

    def say_id(self):
        if self.id < 123456:
            return 'Не верный ID!'
        else:
            return f'Мой ID: {self.id}'



a = NewClass('Maria', 33, 123457)


print(a.say_name(), a.say_age(), a.say_id(), sep='\n')

