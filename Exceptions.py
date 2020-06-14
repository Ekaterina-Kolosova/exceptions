try:
    operator = input('Введите арифметическое действие')
    operand1 = int(input('Введите первое число'))
    operand2 = int(input('Введите второе число'))
    operators = ['+', '-', '*', '/']

    if operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2
    elif operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2

    assert operator in operators, 'Введено неверное арифметическое действие'

    print(f'результат: {result}')
except Exception as e:
    print(e)

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "5455 028765"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_owner_name():
    try:
        document_input = input('Введите номер документа: ')
        for document in documents:
            if document_input == document["number"]:
                print(f'Владелец документа: {document["name"]}')
                break
        else:
            print('Документа с таким номером не существует')
    except KeyError:
        print('Не указано имя владельца')


def get_shelf_number():
    document_input = input('Введите номер документа: ')
    for document in directories.items():
        if document_input in document[1]:
            print(f'Номер полки: {document[0]}')
            break
    else:
        print("Нет документа с таким номером")


def get_list_all_document():
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def add_new_document(folder, directory):
    document_number_input = input('Введите номер документа: ')
    document_type_input = input('Введите тип документа: ')
    document_owner_input = input('Введите имя владельца: ')
    document_shelf_input = input('Введите номер полки: ')
    folder.append({"type": document_type_input, "number": document_number_input, "name": document_owner_input})
    if document_shelf_input in directory.keys():
        directory[document_shelf_input].append(document_number_input)
    else:
        directory.setdefault(document_shelf_input, [document_number_input])
    return folder, directory



def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            get_owner_name()
        elif user_input == 's':
            get_shelf_number()
        elif user_input == 'l':
            get_list_all_document()
        elif user_input == 'a':
            add_new_document(documents, directories)

main()

