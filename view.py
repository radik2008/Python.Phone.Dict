import text_field as txt


def main_menu() -> int:
    print('\x1b[1;3;5;31m   Main menu\x1b[0m')
    print('\x1b[32m1. Просмотреть контакты\x1b[0m')
    print('\x1b[32m2. Создать контакт\x1b[0m')
    print('\x1b[32m3. Удалить контакт\x1b[0m')
    print('\x1b[32m4. Найти контакт\x1b[0m')
    print('\x1b[32m5. Изменить контакт\x1b[0m')
    print('\x1b[32m6. Выход\x1b[0m')
    while True:
        choice = input("\x1b[36mВведите номер меню: \x1b[0m")
        print()
        if choice.isdigit() and 0 < int(choice) < 7:
            return int(choice)
        else:
            print('\x1b[1;31mНеверный выбор, попробуйте еще раз\x1b[0m')


def show_contactc(books: list, messadge: str):
    if books:
        print('-' * 80)
        print("{:<20} {:<20} {:<20} {:<20}".format("Имя", "Фамилия", "Телефон", "Комментарий"))
        for book in books:
            if "Comment" in book:
                comment = book["Comment"]
            else:
                comment = ""
            print("{:<20} {:<20} {:<20} {:<20}".format(book["Name"],
                                                       book["Last Name"],
                                                       book["Phone number"], comment))
        print('-' * 80)
    else:
        print(messadge)


def print_info(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))


def new_contact() -> dict:
    name = input(txt.new_name)
    last_name = input(txt.new_last_name)
    phone_number = input(txt.new_phone_number)
    comment = input(txt.new_comment)
    new_cont = {"Name": name, "Last Name": last_name, "Phone number": phone_number}
    if comment:
        new_cont["Comment"] = comment
    return new_cont


def input_found_contact() -> str:
    name_found = input(txt.name_searce)
    return name_found


def name_contact_delete() -> str:
    name_del = input(txt.name_dellete)
    return name_del

def name_contact_edit() -> str:
    name_editers = input(txt.edit_name)
    return name_editers
