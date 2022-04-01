import csv
from csv import writer
import pandas as pd

from csv import writer


class Robber:
    def __init__(self, name):
        self.name = name

    def scrounge_smthg(self, product_name, count):
        RobberController.scrounge_smthg(self, product_name, count)

    def get_stolen_item(self):
        RobberController.get_stolen_item()

    def __repr__(self):
        return self.name


class RobberController:

    @staticmethod
    def scrounge_smthg(self, product_name, count):
        with open('Thift.csv', 'a') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([self.name] + [product_name] + [count])
            file.close()

    @staticmethod
    def get_stolen_item():
        line = []
        with open('Thift.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                line.append(row[1])

        with open('All_items.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(line)


RobberController = RobberController()
Bob = Robber('Bob')
# Bob.scrounge_smthg('Milk', 10)
# Bob.scrounge_smthg('Candie', 10)
# Bob.scrounge_smthg('Meat', 10)
RobberController.get_stolen_item()

