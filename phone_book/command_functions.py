from colorama import Back, Fore


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return "Contact with this name had already exist."
        elif name.isalpha() and phone.isdigit():
            contacts[name] = phone
            return "Contact added."
        else:
            return "Contact cannot be added. Name  must consist only of letters and phone must consist only of numbers."
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
                return "Contact cannot be updated. Phone must consist only of numbers."
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
                print(
                    f"{Back.BLACK}{Fore.LIGHTBLUE_EX}   Name - {name}, phone - {phone} {Back.RESET}{Fore.RESET}"
                )
            else:
                continue
    else:
        print("   No contacts.")
