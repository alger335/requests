# TODO Задача №2
# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон.
# Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.
#
# Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
# HOST: https://cloud-api.yandex.net:443
#
# Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!
#
# Шаблон для программы
# class YaUploader:
#     def __init__(self, file_path: str):
#         self.file_path = file_path
#
#     def upload(self):
#         """Метод загруджает файлы по списку file_list на яндекс диск"""
#         # Тут ваша логика
#         return 'Вернуть ответ об успешной загрузке'
#
#
# if __name__ == '__main__':
#     uploader = YaUploader('c:\my_folder\file.txt')
#     result = uploader.upload()

from pprint import pprint

import requests
import os


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": "netology", "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, full_path):
        # disk_file_path = os.path.dirname(full_path)
        # print(disk_file_path)
        filename = os.path.basename(full_path)
        # print(filename)
        href = self._get_upload_link().get("href", "")
        # print(filename)
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")




# class YandexDisk:
#
#     def __init__(self, token):
#         self.token = token
#
#     def get_headers(self):
#         return {
#             'Content-Type': 'application/json',
#             'Authorization': 'OAuth {}'.format(self.token)
#         }
#
#     def get_files_list(self):
#         files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
#         headers = self.get_headers()
#         response = requests.get(files_url, headers=headers)
#         return response.json()
#
#     def _get_upload_link(self, disk_file_path):
#         upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
#         headers = self.get_headers()
#         params = {"path": disk_file_path, "overwrite": "true"}
#         response = requests.get(upload_url, headers=headers, params=params)
#         pprint(response.json())
#         return response.json()
#
#     def upload_file_to_disk(self, disk_file_path, filename):
#         href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
#         response = requests.put(href, data=open(filename, 'rb'))
#         response.raise_for_status()
#         if response.status_code == 201:
#             print("Success")