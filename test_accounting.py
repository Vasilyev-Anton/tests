import pytest
from accounting import search_shelf, search_name, add_new_doc

TEST_DATA = [
    ('2207 876234', 'Василий Пупкин', 'Полка № 1'),
    ('11-2', 'Геннадий Покемонов', 'Полка № 1'),
    ('10006', 'Аристарх Павлов', 'Полка № 2'),
    ('53-23', 'Такого документа нет', 'Полка с данным документом отсутствует')
]

TEST_DATA_1 = [
    ('2207 876234', '1', 'Данный документ уже имеется в базе данных'),
    ('53-23', '4', 'Невозможно разместить документ, такой полки не существует'),
    ('53-23', '2', 'Данные успешно внесены!')
]


class TestAccounting:

    @pytest.mark.parametrize('user_input, expected_result, expected_result_1', TEST_DATA)
    def test_search_name(self, user_input, expected_result, expected_result_1):
        assert search_name(user_input) == expected_result

    @pytest.mark.parametrize('user_input, expected_result, expected_result_1', TEST_DATA)
    def test_search_shelf(self, user_input, expected_result, expected_result_1):
        assert search_shelf(user_input) == expected_result_1

    @pytest.mark.parametrize('number_doc, shelf, expected_result', TEST_DATA_1)
    def test_add_new_doc(self, number_doc, shelf, expected_result):
        assert add_new_doc(number_doc, shelf) == expected_result
