def total_salary(path):
    total_salaries = 0
    amount_of_workers = 0

    with open(path, "r", encoding="UTF-8") as file:
        while True:
            line = file.readline()
            if line:
                line_parts = line.split(",")
                salary = int(line_parts[1])
                total_salaries += salary
                amount_of_workers += 1
            else:
                break

    average_salary = int(total_salaries / amount_of_workers)
    result = [total_salaries, average_salary]
    return set(result)


try:
    (total, average) = total_salary("salaries.txt")
    print(f"Total salary: {total}, Average salary: {average}")
except Exception as error:
    print(f"Error - {error}")


# Expected result:
# Total salary: 20800, Average salary: 2080
