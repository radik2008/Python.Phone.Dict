import view
import model
import text_field as txt


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                view.print_info(txt.load_successful)
                pb = model.get_contacts()
                view.show_contactc(pb, txt.no_contact_or_file)
            case 2:
                n_contact = view.new_contact()
                model.create_contact(n_contact)
                view.print_info(txt.add_successful)
            case  3:
                delet_name = view.name_contact_delete()
                found_dict_del = model.search_contact(delet_name)
                if model.delete_contact(found_dict_del):
                    view.print_info(txt.delete_successful)
                else:
                    view.print_info(txt.contact_no_found)
            case 4:
                found_name = view.input_found_contact()
                found_dict = model.search_contact(found_name)
                view.show_contactc(found_dict, txt.contact_no_found)
            case 5:
                edit_name = view.name_contact_edit()
                found_dict_edit = model.search_contact(edit_name)
                new_edit_new_contact = view.new_contact()
                model.edit_contact(found_dict_edit, new_edit_new_contact)
                view.print_info(txt.edit_successful)

            case 6:
                view.print_info(txt.exit)
                exit()
