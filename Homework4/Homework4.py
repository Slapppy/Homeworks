import os
import shutil
import requests

response = requests.get('https://reqres.in/api/users?page=2')
currencies = response.json()['data']
path_ = '/Users/maratahmetov/PycharmProjects/Homeworks/Homework4/users_data/'


def parse_data(path_to_save):
    for i in range(len(currencies)):
        img = requests.get(currencies[i]['avatar'], stream=True)
        path = path_to_save + str(currencies[i]['id'])
        try:
            os.mkdir(path)
            with open(path + '/avatar.png', 'wb') as f:
                shutil.copyfileobj(img.raw, f)
            with open(path + "/user_info.txt", "w") as file:
                file.writelines(f"{str(currencies[i]['email'])}, "
                                f"{str(currencies[i]['first_name'])} {str(currencies[i]['last_name'])}")
        except OSError:
            continue


parse_data(path_)
