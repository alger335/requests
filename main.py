from yandex import YaUploader
from heroes import *


if __name__ == '__main__':
    smartest_hero(get_heroes(['Hulk', 'Captain America', 'Thanos']))
    ya = YaUploader(token="")
    ya.upload_file_to_disk("D:/IT/Python/netology/Full_Course/requests/test.txt")

