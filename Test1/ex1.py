from _csv import writer
from random import randint


class Queue:
    def __init__(self):
        self.list = []
        self.lenght = 0

    def get_list(self):
        return self.list

    def add_item(self, item):
        self.list.append(str(item))
        self.lenght += 1

    def clear(self, ):
        self.list = []
        self.lenght = 0

    def contains(self, elem):
        if elem in self.list:
            return f'Элемент {elem} найден'
        else:
            return 'Такого элемента нет'

    def remove(self):
        if self.lenght == 0:
            raise ValueError('Список пуст!')
        else:
            del self.list[-1]
            self.lenght -= 1


class Screw:
    def __init__(self, height, width, length, weight, color=None):
        self.color = color
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height

    def __str__(self):
        return f"Деталь 1: {self.height}, {self.width}, {self.length}, {self.weight}, {self.color}"


class Storehouse:
    def __init__(self):
        self.storage = Queue()

    def add(self, items):
        self.storage.add_item(items)

    def save(self,):
        file = open('items.txt', 'w', encoding='utf8')
        file.write(f'В Цеху количество деталей {self.storage.lenght}:\n')
        for i in self.storage.list:
            file.write(f'{i}\n')

    def get_list(self):
        self.storage.get_list()


item = Screw(10, 10, 10, 10, 'Black')
item2 = Screw(10, 10, 10, 10, 'Red')
warehouse = Storehouse()

warehouse.add(item)
warehouse.add(item2)
warehouse.save()

