import view
import model
import text

copy_open_file = model.open_file()
def link_new_PB_copy(copy_file):
    view.text_print(text.pb_link)
    model.print_phone_book(copy_file)

def start(copy_open_PB: list):
    while True:
        choice = view.menu()

        match choice:
            case 1:
                model.print_phone_book(copy_open_PB)
            case 2:
                copy_open_PB = model.add_contact(copy_open_PB)
                view.text_print(text.successful)
                link_new_PB_copy(copy_open_PB)
            case 3:
                found = model.search_contact(copy_open_PB)
                view.f_string_print(text.search_link, found)
            case 4:
                copy_open_PB = model.change_contact(copy_open_PB)
                link_new_PB_copy(copy_open_PB)
            case 5:
                copy_open_PB = model.delete_contact(copy_open_PB)
                view.text_print(text.successful)
                link_new_PB_copy(copy_open_PB)
            case 6:
                view.save_file_func(model.save_file, copy_open_PB)
            case 7:
                break
