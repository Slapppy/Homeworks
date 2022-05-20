import os
import shutil
import numpy as np
import threading
import requests

path_ = '../Homework5/users_data/'


def parse_users(users, path_to_save):
    for user in users:
        try:
            img = requests.get(user['avatar'], stream=True)
            path = path_to_save + str(user['id'])
            os.mkdir(path)
            with open(path + '/avatar.png', 'wb') as f:
                shutil.copyfileobj(img.raw, f)
            with open(path + "/user_info.txt", "w") as file:
                file.writelines(f"{str(user['email'])}, "
                                f"{str(user['first_name'])} {str(user['last_name'])}")
        except OSError:
            continue



def get_users(pages):
    users = []
    for page in pages:
        response = requests.get(f'https://reqres.in/api/users?page={page}')
        currencies = response.json()['data']
        users.extend(currencies)
    return users


def start_thread(path_to_save, users):
    users = get_users(users)
    threads = []
    for list_slice in np.array_split(users, 4):
        thread = threading.Thread(target=parse_users, args=(list(list_slice), path_to_save))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


start_thread(path_, [1])


