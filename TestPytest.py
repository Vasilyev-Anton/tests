import pytest
from main import search_shelf, search_name, documents, directories, add_new_doc

TEST_DATA = [
    ('2207 876234', 'Василий Пупкин', 'Полка № 1', 'Данный документ уже имеется в базе данных'),
    ('11-2', 'Геннадий Покемонов', 'Полка № 1', 'Данный документ уже имеется в базе данных'),
    ('10006', 'Аристарх Павлов', 'Полка № 2', 'Данный документ уже имеется в базе данных'),
    ('55-23', 'Такого документа нет', 'Полка с данным документом отсутствует', 'Данные успешно внесены!')
]


class TestPytest:

    @pytest.mark.parametrize('user_input, expected_result, expected_result_1, expected_result_2', TEST_DATA)
    def test_search_name(self, user_input, expected_result, expected_result_1, expected_result_2):
        assert search_name(user_input, docs=documents) == expected_result

    @pytest.mark.parametrize('user_input, expected_result, expected_result_1, expected_result_2', TEST_DATA)
    def test_search_shelf(self, user_input, expected_result, expected_result_1, expected_result_2):
        assert search_shelf(user_input, direct=directories) == expected_result_1

    @pytest.mark.parametrize('user_input, expected_result, expected_result_1, expected_result_2', TEST_DATA)
    def test_add_new_doc(self, user_input, expected_result, expected_result_1, expected_result_2):
        assert add_new_doc(number_doc=user_input, name=expected_result, docs=documents, direct=directories, type_doc='passport',
                           shelf='2') == expected_result_2
