import pytest

from Homework1.Homework1 import Human, Queue


class TestHuman:

    @pytest.fixture()
    def create_human(self, name, age, gender):
        return Human(name, age, gender)

    @pytest.fixture()
    def create_queue(self):
        return Queue()

    def takeaqueae_test(self, human, queue, create_human, create_queue):
        assert human.takeaqueae() == queue.list.find(human)


if __name__ == '__main__':
    pass


