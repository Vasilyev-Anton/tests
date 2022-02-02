
import requests

res_dict = dict()


class YaDisk:

    def __init__(self, token_ya):
        self.token_ya = token_ya

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token_ya}'}

    def create_folder(self, disk_file_path):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        folder_params = {'path': disk_file_path}
        response = requests.put(url=folder_url, params=folder_params, headers=headers)
        return response.status_code
        # return response.json()

    def delete_folder(self, disk_file_path):
        headers = self.get_headers()
        folder_params = {'path': disk_file_path, 'permanently': True}
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.delete(url=folder_url, params=folder_params, headers=headers)
        return response.status_code
