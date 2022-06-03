import os
import numpy as np
import threading
import requests

path_ = 'planet_data/'

def parse_users(planet, path_to_save):
    for planets in planet:
        # проверка на данные если их не пропускаем
        if len(planets['collection']['items']) == 0:
            continue
        path = path_to_save + str(planets['collection']['href'][42:52])
        os.mkdir(path)
        # запись заголовка
        with open(path + "/title.txt", "w") as file:
            title = planets['collection']['items'][0]['data'][0]['title']
            file.writelines(f"{str(title)}")
        # запись описания
        with open(path + "/description.txt", "w") as file:
            file.writelines(f"{str(planets['collection']['items'][0]['data'][0]['description'])}")


# получение планет
def get_planet():
    images = []
    for page in range(1, 31):
        response = requests.get(f'https://images-api.nasa.gov/search?q=earth%2022-05-{page}&media_type=image')
        currencies = response.json()
        images.append(currencies)
    return images




# запуск в 4 потоках
def start_thread(path_to_save):
    users = get_planet()
    threads = []
    for list_slice in np.array_split(users, 4):
        thread = threading.Thread(target=parse_users, args=(list(list_slice), path_to_save))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


start_thread(path_)


