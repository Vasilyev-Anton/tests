
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Пупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def search_name(user_input, docs=documents):
    # user_input = input('Введите номер документа: ')
    for people in docs:
        if user_input == people['number']:
            return people['name']
    else:
        return 'Такого документа нет'


def search_shelf(user_input, direct=directories):
    # user_input = input('Введите номер документа: ')
    for key, value in direct.items():
        for number in value:
            if user_input == number:
                return f'Полка № {key}'
    else:
        return 'Полка с данным документом отсутствует'


def print_data(docs):
    el_str = list()
    for value in docs:
        el_str.append(" ".join(value.values()))
    return el_str


def add_new_doc(number_doc, shelf, docs=documents, direct=directories, type_doc='passport', name='Anton'):
    # type_doc = input('Введите тип документа: ')
    # number_doc = input('Введите номер документа: ')
    for data in docs:
        if number_doc in data.values():
            return 'Данный документ уже имеется в базе данных'
        else:
            # name = input('Введите имя и фамилию владельца документа: ')
            # shelf = input('Введите номер полки для документа:')
            if shelf not in direct.keys():
                return 'Невозможно разместить документ, такой полки не существует'
            else:
                new_dict = {'type': type_doc, 'number': number_doc, 'name': name}
                docs.append(new_dict)
                for key in direct.keys():
                    if shelf == key:
                        direct[key].append(number_doc)
                        return 'Данные успешно внесены!'


def help_menu():
    """
 Quit: выход из программы
    p: выводит имя и фамилию человека по номеру документа
    s: выводит номер полки по номеру документа
    l: выводит весь список данных
    a: добавляет новый документ в базу данных
"""


# def main(docs, direct):
#     while True:
#         user_input = input('Введите команду/"Help" для справки: ')
#         if user_input == 'p':
#             print(search_name(docs))
#         elif user_input == 's':
#             print(search_shelf(direct))
#         elif user_input == 'l':
#             print(print_data(docs))
#         elif user_input == 'a':
#             add_new_doc(docs, direct)
#         elif user_input.lower() == 'help':
#             help(help_menu)
#         elif user_input.lower() == 'quit':
#             print('Выход из программы')
#             break


# main(docs=documents, direct=directories)
