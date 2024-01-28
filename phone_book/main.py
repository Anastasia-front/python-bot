from colorama import Back, Fore
from command_functions import (
    add_contact,
    change_contact,
    delete_contact,
    parse_input,
    show_all,
    show_contact,
)

commands = [
        "hello",
        "add [name] [phone]",
        "change [name] [phone]",
        "delete [name]",
        "contact [name]",
        "contacts",
        "commands",
        "close/exit",
    ]


def main():
    contacts = {}

    print(f"{Back.WHITE}Welcome to the assistant bot for phone book 📲 {Back.RESET}")

    while True:
        user_input = input(f"{Back.YELLOW}Enter a command:{Back.RESET}  ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Back.CYAN}Good bye!{Back.RESET}")
            break

        elif command == "hello":
            print(f"{Back.GREEN}How can I help you?{Back.RESET}")

        elif command == "add":
            print(f"{Fore.CYAN}   {add_contact(args, contacts)} {Fore.RESET}")

        elif command == "change":
            print(
                f"{Fore.LIGHTGREEN_EX}   {change_contact(args, contacts)} {Fore.RESET}"
            )

        elif command == "delete":
            print(f"{Fore.GREEN}   {delete_contact(args, contacts)} {Fore.RESET}")

        elif command == "contact":
            print(
                f"{Fore.LIGHTMAGENTA_EX}   {show_contact(args, contacts)} {Fore.RESET}"
            )

        elif command == "contacts":
            show_all(contacts)

        elif command == "commands":
            for command in commands:
                print(f"{Fore.LIGHTYELLOW_EX}   {command} {Fore.RESET}")

        else:
            print(f"{Fore.RED}   Invalid command. {Fore.RESET}")


if __name__ == "__main__":
    main()
