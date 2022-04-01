from csv import writer
import pandas as pd
from datetime import datetime
from random import randint


class User:
    def __init__(self, name, ser_name, ):
        self.ser_name = ser_name
        self.name = name

    def send_message(self, message, to):
        with open('messages.csv', 'a') as f_object:
            writer_object = writer(f_object, delimiter=',')
            writer_object.writerow([randint(10000, 99999)] +
                                   [self.name + " " + self.ser_name] + [to] + [message] + [datetime.now()])
            f_object.close()

    def delete_message(self, id):
        df = pd.read_csv('messages.csv', delimiter=',', header=None)
        df.columns = ['idx', 'from', 'to', 'message', 'time']
        df.set_index('idx', inplace=True)
        result = df.drop(id)
        return result.to_csv('messages.csv', header=False)

    def __repr__(self):
        return self.name + " " + self.ser_name


class UserController:

    @staticmethod
    def get_all_messages(first_user, second_user):
        chat_df = pd.read_csv('messages.csv', delimiter=',', header=None)
        chat_df.columns = ['idx', 'from_', 'to_', 'message', 'time']
        result = chat_df[(chat_df.from_ == first_user) & (chat_df.to_ == second_user)
                         | (chat_df.to_ == first_user) & (chat_df.from_ == second_user)]
        return result.to_csv('Chat.csv', header=False)


Vasiya = User('Вася', 'Пупкин')
Vova = User('Вова', 'Лисин')
Bob = User('Bob', 'Kelly')
Tom = User('Tom', 'Ford')

userConroller = UserController
userConroller.get_all_messages('Tom Ford', 'Bob Kelly')
