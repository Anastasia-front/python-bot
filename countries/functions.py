from colorama import Back


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def show_country_info(country):
    return f"{Back.LIGHTBLUE_EX + country['name']+ Back.RESET} \n \
            info : \n\
            population - {formatting_number(country['population'])} people\n\
            size - {formatting_number(country['size'])} km²"


def show_countries(countries):
    if len(countries) != 0:
        for country in countries:
            if country:
                print(country["name"])
            else:
                continue
    else:
        print("No countries.")


def show_country_all_info(args, countries):
    name = args[0]
    if len(countries) != 0:
        for country in countries:
            if country["name"].lower() == name.lower():
                return show_country_info(country)
    else:
        return "No countries."


def show_countries_all_info(countries):
    if len(countries) != 0:
        for country in countries:
            if country:
                print(show_country_info(country))
    else:
        print("No countries.")


def max_statistic(args, countries, key):
    stats = {}
    measure = "km²" if key == "size" else "people"

    if len(args) >= 2:
        for name in args:
            found = False
            name = name.lower()
            for country in countries:
                current_country = country["name"].lower()
                if current_country == name and not found:
                    stats[name] = country[key]
                    found = True
            if not found:
                return f"{name} country not found."

        max_country = max(stats, key=stats.get)
        max_value = formatting_number(stats[max_country])

        result = f"The highest {key} is in {max_country.title()}, which has {max_value} {measure}."

        return result
    else:
        return "You did not enter min 2 countries."


def min_statistic(args, countries, key):
    stats = {}
    measure = "km²" if key == "size" else "people"

    if len(args) >= 2:
        for name in args:
            found = False
            name = name.lower()
            for country in countries:
                current_country = country["name"].lower()
                if current_country == name and not found:
                    stats[name] = country[key]
                    found = True
            if not found:
                return f"{name} country not found."

        min_country = min(stats, key=stats.get)
        min_value = formatting_number(stats[min_country])

        result = f"The lowest {key} is in {min_country.title()}, which has {min_value} {measure}."

        return result
    else:
        return "You did not enter min 2 countries."


def formatting_number(number):
    formatted_number = f"{number:,}".replace(",", "_")
    return formatted_number
