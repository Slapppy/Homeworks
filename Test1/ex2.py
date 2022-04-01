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
        with open('Thift.csv', 'a') as f_object:
            writer_object = writer(f_object, delimiter=',')
            writer_object.writerow([self.name] + [product_name] + [count])
            f_object.close()

    @staticmethod
    def get_stolen_item():
        thift_df = pd.read_csv('Thift.csv', delimiter=',', header=None)
        thift_df.columns = ['Name', 'Item', 'count']
        result = thift_df['Item']
        return result.to_csv('All_items.csv', header=False)


RobberController = RobberController()
Bob = Robber('Bob')
Bob.scrounge_smthg('Milk', 10)
Bob.scrounge_smthg('Candie', 10)
Bob.scrounge_smthg('Meat', 10)
RobberController.get_stolen_item()
