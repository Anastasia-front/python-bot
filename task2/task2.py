def get_cats_info(path):
    cats_info = []

    with open(path, "r", encoding="UTF-8") as file:
        while True:
            line = file.readline()
            if line:
                line_parts = line.split(",")
                id = line_parts[0]
                name = line_parts[1]
                age = line_parts[2]
                age = age.strip()
                cat = {}
                cat["id"] = id
                cat["name"] = name
                cat["age"] = age
                cats_info.append(cat)
            else:
                break
    return cats_info


try:
    cats_info = get_cats_info("cats.txt")
    print(cats_info)
except Exception as error:
    print(f"Error - {error}")

# Expected result:

# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]
