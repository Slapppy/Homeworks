from random import randint


class Human:
    def __init__(self, name, age, gender):
        self.gender = gender
        self.age = age
        self.name = name

    def takeaqueae(self, que):
        return Queue.static_add_person(que, self)

    def __repr__(self):
        return self.name


class Queue:
    def __init__(self):
        self.list = []
        self.lenght = 0

    @staticmethod
    def static_add_person(que, human):
        return que.add_item(human)

    def add_item(self, human):
        self.list.append(human)
        self.lenght += 1

    def clear(self, ):
        self.list = []
        self.lenght = 0

    def contains(self, elem: Human):
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

    def rnd_insert(self, name ,age , gender):
        if len(self.list) == 0:
            self.add_item(Human(name,age,gender))
        else:
            self.list.insert(randint(1, len(self.list)), Human(name,age,gender))


store = Queue()

tom = Human('Tom', 12, 'gay')
tom.takeaqueae(store)
bob = Human('Bob', 12, 'gay')
bob.takeaqueae(store)
dick = Human('Dick', 12, 'gay')
dick.takeaqueae(store)
store.rnd_insert('Dick3', 12, 'gay')

print(store.list)