import view
import model
import text

my_PB = model.PhoneBook()
copy_open_file = my_PB.open_file()
def link_new_PB_copy(copy_file):
    view.text_print(text.pb_link)
    my_PB.print_phone_book(copy_file)

def start(copy_open_PB: list):
    while True:
        choice = view.menu()

        match choice:
            case 1:
                my_PB.print_phone_book(copy_open_PB)
            case 2:
                copy_open_PB = my_PB.add_contact(copy_open_PB)
                view.text_print(text.successful)
                link_new_PB_copy(copy_open_PB)
            case 3:
                found = my_PB.search_contact(copy_open_PB)
                view.f_string_print(text.search_link, found)
            case 4:
                copy_open_PB = my_PB.change_contact(copy_open_PB)
                link_new_PB_copy(copy_open_PB)
            case 5:
                copy_open_PB = my_PB.delete_contact(copy_open_PB)
                view.text_print(text.successful)
                link_new_PB_copy(copy_open_PB)
            case 6:
                view.save_file_func(my_PB.save_file, copy_open_PB)
            case 7:
                break
