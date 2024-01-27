from colorama import Back
from functions import (
    max_statistic,
    min_statistic,
    parse_input,
    show_countries,
    show_countries_all_info,
    show_country_info,
)


def main():
    countries = []
    with open("country_comparison/countries.txt", "r", encoding="UTF-8") as file:
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

    print(Back.LIGHTRED_EX + "Welcome to the assistant bot" + Back.RESET)

    while True:
        user_input = input(Back.CYAN + "Enter a command:" + Back.RESET + "  ")
        command, *args = parse_input(user_input)

        if command in ["bye", "thanks"]:
            print(Back.MAGENTA + "Have a good day" + Back.RESET)
            break

        elif command in ["hi", "hello"]:
            print(Back.YELLOW + "How can I help you?" + Back.RESET)

        elif command == "country":
            print(
                Back.LIGHTMAGENTA_EX + show_country_info(args, countries) + Back.RESET
            )

        elif command == "countries":
            (show_countries(countries))

        elif command == "countries-all-info":
            (show_countries_all_info(countries))

        elif command == "max-population":
            print(
                Back.LIGHTGREEN_EX
                + max_statistic(args, countries, "population")
                + Back.RESET
            )

        elif command == "max-size":
            print(
                Back.LIGHTWHITE_EX + max_statistic(args, countries, "size") + Back.RESET
            )

        elif command == "min-population":
            print(
                Back.LIGHTYELLOW_EX
                + min_statistic(args, countries, "population")
                + Back.RESET
            )

        elif command == "min-size":
            print(
                Back.LIGHTCYAN_EX + min_statistic(args, countries, "size") + Back.RESET
            )

        else:
            print(Back.RED + "Invalid command." + Back.RESET)


if __name__ == "__main__":
    main()
