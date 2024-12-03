# Доступ свойств родителя. Переопределение свойств

class Vehicle:
    __COLOR_VARIANTS=['blue','red','green','black']
    def __init__(self,owner,model,engine_power,color ='red'):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def set_color(self,new_color):
        if self.__COLOR_VARIANTS.__contains__(new_color.lower()):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец:',self.owner)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos','Toyota Mark II',500)

vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
