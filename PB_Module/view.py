import text

def text_print(txt):
    return print(txt)

def f_string_print(txt, argument):
    return print(f'{txt}:\n{argument}')

def text_input(txt):
    return input(txt)


pb_link_print = print(text.pb_link)
def menu():
    print(text.open_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)

# def print_PB():

def add_contact_data():
    first_name = input(text.first_name_txt)
    second_name = input(text.second_name_txt)
    phone_number = input(text.phone_number_txt)
    comment = input(text.comment_txt) + '\n'
    return ' '.join([first_name, second_name, phone_number, comment])

def save_file_func(operacion, copy_file):
    ans = input(text.save_diff).lower()
    if ans == 'y':
        operacion(copy_file)
        print(text.successful)
    else:
        print(text.not_save)