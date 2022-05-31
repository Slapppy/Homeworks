import random
import string
import pytest

from Homework1.Homework1 import Human, Queue


class TestQueue:
    que = Queue()

    @pytest.fixture()
    def create_que(self):
        return self.que

    @pytest.fixture()
    def create_human(self):
        name = ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
        age = random.randint(0, 101)
        human = Human(name, age, 'gay')
        self.que.add_item(human)
        return human

    def test_clear(self, create_que, create_human):
        create_human
        assert create_que.clear() == create_que.lenght

    def test_remove(self, create_que, create_human):
        create_human
        assert create_que.remove() == create_que.lenght

    def test_contains(self, create_que, create_human):
        create_human
        assert create_que.contains(create_human) == create_human
