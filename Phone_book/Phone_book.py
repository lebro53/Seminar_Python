# Открывать файл .тхт
# Сохранить файл
# Показать все контакты
# Добавить контакт
# Найти контакт
# Изменить контакт
# Удалить контакт
# Выход
# Имя телефон и коментарий
path = 'Phone_book.txt'


def open_file() -> list:
    with open(path, 'r', encoding='UTF-8') as file:
        text = file.readlines()
    return text


def save_file(copy_file) -> None:
    with open(path, 'w', encoding='UTF-8') as file:
        new_text = (''.join(copy_file))
        file.write(new_text)


print(open_file())


def print_phone_book(operation) -> None:
    new_text = ''
    for i in operation:
        new_text += str(i)
    print(new_text)


def add_contact(copy_file: list) -> list:
    first_name = '\n'+input('Введите имя контакта: ')
    second_name = input('Введите фамилию контакта: ')
    phone_number = input('Введите телефон контакта: ')
    comment = input('Введите коментарий для контакта: ') + '\n'
    new_contact_list = ' '.join([first_name, second_name, phone_number, comment])
    copy_file.append(new_contact_list)
    return copy_file


def search_contact(copy_file):
    search = input('Если вы хотите осуществить поиск по имени и фамилии, поставьте знак +. Если по номеру знак -.')
    all_contact = [i.lower() for i in copy_file]
    found_contact = ''
    if search == '+':
        first_name = input('Введите имя искомого контакта: ').lower()
        second_name = input('Введите фамилию искомого контакта: ').lower()
        for i in all_contact:
            if first_name in i and second_name in i:
                found_contact += i
    else:
        number = input('Введите номер искомого контакта: ')
        for i in all_contact:
            if number in i:
                found_contact += i
    if found_contact == '':
        print('Контакт не существует')
    return found_contact


def change_contact(copy_file: list) -> list:
    all_contacts = ''
    cnt = 1
    for i in copy_file:
        all_contacts += str(cnt) + '.' + ' ' + i
        cnt += 1
    print(f'Найденые контакты: \n{all_contacts}')
    what_to_change = int(input('Введите номер контакта, который хотите поменять: '))
    new_information = input('Введите новую информацию (имя, фамилию, номер телефона, коментарий): ') + '\n'
    copy_file[what_to_change-1] = new_information
    return copy_file

def delete_contact(copy_file: list):
    all_contacts = ''
    cnt = 1
    for i in copy_file:
        all_contacts += str(cnt) + '.' + ' ' + i
        cnt += 1
    print(f'Найденые контакты: \n{all_contacts}')
    delete_name = int(input('Введите номер строки который хотите удалить: '))
    del copy_file[delete_name - 1]
    return copy_file


def menu(copy_file):
    print(
        'Доступные команды: /command - показывает список команд, /all - все контакты, \n'
        '/add - добавить контакт, /search - поиск контакта, /change - изменить контакт, \n'
        '/delete - удалить контакт, /save- сохраняет все изменения, /exit - выйти из программы')
    while True:
        menu = input('Введите действие: ')
        if menu == '/command':
            print('Доступные команды: /command - показывает список команд, /all - все контакты, \n'
                  '/add - добавить контакт, /search - поиск контакта, /change - изменить контакт, \n'
                  '/delete - удалить контакт, /save- сохраняет все изменения, /exit - выйти из программы')
            continue
        if menu == '/all':
            print_phone_book(copy_file)
            continue
        if menu == '/add':
            copy_file = add_contact(copy_file)
            print('Контакт успешно добавлен.')
            print('Теперь телефонный справочник выглядит так: ')
            print_phone_book(copy_file)
            continue
        if menu == '/search':
            found = search_contact(copy_file)
            print(f'Нашли следующие варианты:\n{found}')
            continue
        if menu == '/change':
            copy_file = change_contact(copy_file)
            print('Теперь телефонный справочник выглядит так: ')
            print_phone_book(copy_file)
            continue
        if menu == '/delete':
            copy_file = delete_contact(copy_file)
            print('Контакт успешно удален')
            print('Теперь телефонный справочник выглядит так: ')
            print_phone_book(copy_file)
            continue
        if menu == '/save':
            ans = input('Хотите сохранить изменения? Введите: Y/N: ').lower()
            if ans == 'да':
                save_file(copy_file)
                print('Успешно')
            else:
                print('Изменения отменены')
            continue
        if menu == '/exit':
            print('До скорых встреч')
            break


copy_open_file = open_file()
menu(copy_open_file)
