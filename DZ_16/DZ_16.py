# Необходимо создать класс Human с атрибутами:
# name
# surname
# age
# phone
# address
# Атрибуты должны заполняться в методе __init__
# Так-же нужно написать методы:
# get_info() - который возвращает словарь в котором находится информация о человеке
# call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
# Нужно создать 3 обьекта класса Human и вызвать у них метод get_info

class Human:
    
    def __init__(self, name, surname, age, phone, adress):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.adress = adress

    def get_info(self):
        return dict(name=self.name, surname=self.surname, age=self.age, phone=self.phone, adress=self.adress)

    def call(self, phone_number):
        print(f"{self.phone} вызывает абонента {phone_number}")


vasia = Human('vasia', 'pupkin', 20, '0991111111', 'kiev')
petia = Human('petia', 'mupkin', 21, '0992222222', 'lviv')
kolia = Human('kolia', 'tupkin', 22, '0993333333', 'odessa')

print(vasia.get_info())
print(petia.get_info())
print(kolia.get_info())
