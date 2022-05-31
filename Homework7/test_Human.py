import random
import string
import pytest

from Homework1.Homework1 import Human, Queue


class TestHuman:

    @pytest.fixture()
    def create_human(self):
        name = ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
        age = random.randint(0, 101)
        return Human(name, age, 'gay')

    @pytest.fixture()
    def create_queue(self):
        return Queue()

    def test_takeaqueae(self, create_human, create_queue):
        assert create_human.takeaqueae(create_queue) == create_queue.contains(create_human)

