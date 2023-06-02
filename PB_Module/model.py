import view
import text

path = 'pb.txt'


def open_file() -> list:
    with open(path, 'r', encoding='UTF-8') as file:
        return file.readlines()


def print_phone_book(operation) -> None:
    new_text = ''
    for i in operation:
        new_text += str(i)
    print(new_text)

def add_contact(copy_file: list) -> list:
    new_contact_list = view.add_contact_data()
    copy_file.append(new_contact_list)
    return copy_file

def search_contact(copy_file):
    all_contact = [i.lower() for i in copy_file]
    found_contact = ''
    search_info = view.text_input(text.search_contact).lower()
    for i in all_contact:
        if search_info in i:
            found_contact += i
    if found_contact == '':
        view.text_print(text.contact_not_found)
    return found_contact


def change_contact(copy_file: list) -> list:
    all_contacts = ''
    cnt = 1
    for i in copy_file:
        if '\n' not in i:
            all_contacts += str(cnt) + '.' + ' ' + i + '\n'
        else:
            all_contacts += str(cnt) + '.' + ' ' + i
        cnt += 1
    view.f_string_print(text.search_link, all_contacts)
    what_to_change = int(view.text_input(text.swap_information))
    new_information = view.text_input(text.new_information_to_swap) + '\n'
    copy_file[what_to_change - 1] = new_information
    return copy_file

def delete_contact(copy_file: list):
    all_contacts = ''
    cnt = 1
    for i in copy_file:
        all_contacts += str(cnt) + '.' + ' ' + i
        cnt += 1
    view.f_string_print(text.search_link, all_contacts)
    delete_name = int(view.text_input(text.del_contact))
    del copy_file[delete_name - 1]
    return copy_file

def save_file(copy_file) -> None:
    with open(path, 'w', encoding='UTF-8') as file:
        new_text = (''.join(copy_file))
        file.write(new_text)