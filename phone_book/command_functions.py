def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        if name.isalpha() and phone.isdigit():
            contacts[name] = phone
            return "Contact added."
        else:
            return "Contact cannot be added. Name  must consist of letters and phone must consist of numbers."
    except Exception as error:
        return f"You entered not correct information. The error is '{error}'."


def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            if phone.isdigit():
                contacts[name] = phone
                return "Contact updated."
            else:
                return "Contact cannot be updated. Phone must consist of numbers."
        else:
            return "Contact not found."
    except Exception as error:
        return f"You entered not correct information. The error is '{error}'"


def delete_contact(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            del contacts[name]
            return "Contact deleted."
        else:
            return "Contact not found."
    except Exception as error:
        return f"You entered not correct information. The error is '{error}'"


def show_contact(args, contacts):
    if len(args) > 0:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "You did not enter username."


def show_all(contacts):
    if len(contacts) != 0:
        for name, phone in contacts.items():
            if name != "" and phone != "":
                print(f"Name - {name}, phone - {phone}")
            else:
                continue
    else:
        return "No contacts."
