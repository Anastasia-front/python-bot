from colorama import Back, Fore
from command_functions import (
    add_contact,
    change_contact,
    delete_contact,
    parse_input,
    show_all,
    show_contact,
)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input(f"{Back.YELLOW} Enter a command:{Back.RESET}")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Fore.YELLOW} Good bye! {Fore.RESET}")
            break

        elif command == "hello":
            print(f"{Back.GREEN} How can I help you? {Back.RESET}")

        elif command == "add":
            print({Fore.CYAN} + add_contact(args, contacts) + {Fore.RESET})

        elif command == "change":
            print({Fore.LIGHTWHITE_EX} + change_contact(args, contacts) + {Fore.RESET})

        elif command == "delete":
            print({Fore.LIGHTRED_EX} + delete_contact(args, contacts) + {Fore.RESET})

        elif command == "phone":
            print({Fore.LIGHTMAGENTA_EX} + show_contact(args, contacts) + {Fore.RESET})

        elif command == "all":
            show_all(contacts)

        else:
            print(f"{Fore.RED} +Invalid command. {Fore.RESET}")


if __name__ == "__main__":
    main()
