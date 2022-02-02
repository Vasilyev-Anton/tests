import json
import pytest
from yadisk import YaDisk

with open('config.json') as f:
    config = json.load(f)

TOKEN = config['token_ya']
FOLDER = 'test1'
TEST_DATA = [(TOKEN, FOLDER, 201), ('ccccccccccccccccccc', FOLDER, 401), (TOKEN, FOLDER, 409)]


class TestYaDisk:
    @classmethod
    def teardown_class(cls):
        ya = YaDisk(TOKEN)
        ya.delete_folder(FOLDER)

    @pytest.mark.parametrize('token, disk_file_path, expected_result', TEST_DATA)
    def test_create_a_folder(self, token, disk_file_path, expected_result):
        ya = YaDisk(token)
        assert ya.create_folder(disk_file_path) == expected_result
