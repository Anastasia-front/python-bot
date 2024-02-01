from colorama import Back, Fore
from functions import (
    max_statistic,
    min_statistic,
    parse_input,
    show_countries,
    show_countries_all_info,
    show_country_all_info,
)

commands = [
    "hi",
    "countries",
    "countries-info",
    "country-info [name]",
    "max-population [name1] [name2] ...",
    "min-population [name1] [name2] ...",
    "max-size [name1] [name2] ...",
    "min-size [name1] [name2] ...",
    '"bye", "thanks"',
]


def main():
    countries = []
    with open("countries/countries.txt", "r", encoding="UTF-8") as file:
        while True:
            line = file.readline()
            if line:
                line_parts = line.split(",")
                country = {}
                name = line_parts[0]
                population = int(line_parts[1])
                size = int(line_parts[2])
                country["name"] = name
                country["population"] = population
                country["size"] = size
                countries.append(country)
            else:
                break

    print(
        f"{Back.LIGHTWHITE_EX}Welcome to the assistant bot \
        for information about countries 🇧🇷 🇲🇽 🇨🇳 🇮🇳 🇮🇩 🇺🇸 🇧🇩{Back.RESET}"
    )

    while True:
        user_input = input(Back.CYAN + "Enter a command:" + Back.RESET + "  ")
        command, *args = parse_input(user_input)

        if command in ["bye", "thanks"]:
            print(Back.MAGENTA + "Have a good day" + Back.RESET)
            break

        elif command in ["hi"]:
            print(Back.LIGHTBLACK_EX + "What are you interesting in?" + Back.RESET)

        elif command == "country-info":
            print(
                f"{Back.LIGHTMAGENTA_EX}{show_country_all_info(args, countries)}{Back.RESET}"
            )

        elif command == "countries":
            (show_countries(countries))

        elif command == "countries-info":
            (show_countries_all_info(countries))

        elif command == "max-population":
            print(
                f'{Back.LIGHTGREEN_EX}{max_statistic(args, countries, "population")}{Back.RESET}'
            )

        elif command == "max-size":
            print(
                f'{Back.LIGHTWHITE_EX}{max_statistic(args, countries, "size")}{Back.RESET}'
            )

        elif command == "min-population":
            print(
                f'{Back.LIGHTYELLOW_EX}{min_statistic(args, countries, "population")}{Back.RESET}'
            )

        elif command == "min-size":
            print(
                f'{Back.LIGHTCYAN_EX}{min_statistic(args, countries, "size")}{Back.RESET}'
            )

        elif command == "commands":
            for command in commands:
                print(f"{Fore.LIGHTGREEN_EX}{command}{Fore.RESET}")

        else:
            print(Back.RED + "Invalid command." + Back.RESET)


if __name__ == "__main__":
    main()
