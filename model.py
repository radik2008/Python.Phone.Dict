import json

PATH = 'phone_book.json'


def get_contacts():
    with open(PATH, 'r') as file:
        data = json.load(file)
        return data


def create_contact(new_contact: dict):
    with open(PATH, "r") as file:
        contacts = json.load(file)
    contacts.append(new_contact)
    with open(PATH, "w") as file:
        json.dump(contacts, file)


def search_contact(search_word: str) -> list:
    with open(PATH, "r") as data:
        contacts = json.load(data)
    name_found = search_word.lower()
    found_contacts = []
    for contact in contacts:
        if name_found in (contact['Name'] + contact['Last Name'] + contact['Phone number']).lower():
            found_contacts.append(contact)
    return found_contacts


def delete_contact(contacts_to_delete: list) -> bool:
    with open(PATH, "r") as data:
        contacts = json.load(data)
    deleted_all = True
    for contact in contacts_to_delete:
        if contact in contacts:
            contacts.remove(contact)
        else:
            deleted_all = False
    with open(PATH, "w") as data:
        json.dump(contacts, data)
    return deleted_all


def edit_contact(delet_name: list, new_name: dict):
    with open(PATH, "r") as data:
        contacts = json.load(data)
    for contact in delet_name:
        if contact in contacts:
            contacts.remove(contact)
            break
    contacts.append(new_name)
    with open(PATH, "w") as data:
        json.dump(contacts, data)

