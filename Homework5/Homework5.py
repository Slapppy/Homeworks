import os
import shutil
import requests
import threading

page = int(input('Enter the page '))
if page > 2:
    raise ValueError('Число должно быть не больше 2')


response = requests.get(f'https://reqres.in/api/users?page={page}')
currencies = response.json()['data']
path_ = '../Homework5/users_data/'


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


thread1 = threading.Thread(target=parse_data, name='t1', args=[path_])
thread2 = threading.Thread(target=parse_data, name='t2', args=[path_])
thread3 = threading.Thread(target=parse_data, name='t3', args=[path_])
thread4 = threading.Thread(target=parse_data, name='t4', args=[path_])
thread1.start()
thread2.start()
thread3.start()
thread4.start()
