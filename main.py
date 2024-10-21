import fnmatch
import re

cat_breeds = [
    [
        "Abyssinian",
        6,
        10,
        ["Ruddy", "bright red", "blue", "fawn"],
    ],
    [
        "Bengal",
        6,
        18,
        ["Bright orange to light brown, with dark spots", "a distinctive marbling pattern"],
    ],
    [
        "Sphynx",
        6,
        12,
        ["White", "black", "blue", "red", "cream", "chocolate", "lavender", "cinnamon", "fawn"],
    ]
]


def print_info():
    print("****************************************************")
    print("1 - list, 2 - add, 3 - edit, 4 - remove, 5 - exit")
    print("1. Produce description")
    print("2. Add new breed")
    print("3. Edit breed")
    print("4. Remove breed")
    print("5. Filter breeds")
    print("6. Exit")
    print("*****************************************************")


def print_breed(breed, num):
    colour = ""
    for b in breed[3]:
        colour += b + ", "
    print(f"{num}. Cat breed name: {breed[0]}. Weight: {breed[1]}-{breed[2]}. Colours: {colour[:-2]}.")


def print_breeds(breeds=cat_breeds):
    count = 1
    for b in breeds:
        print_breed(b, count)
        count += 1


def add_breed():
    cat_breeds.append(input_breed())


def edit_breed():
    num = int(input("Enter number of the cat breed you want to edit: "))
    print_breed(cat_breeds[num - 1], num)
    print("Enter new values:")
    cat_breeds[num - 1] = input_breed()


def input_breed():
    breed_name = input("What's breed name? ")
    min_weight = int(input("What's minimum weight? "))
    max_weight = int(input("What's maximum weight? "))
    colours = input("Enter colours separated with commas (press enter at the end): ").split(",")
    for i in range(len(colours)):
        colours[i] = colours[i].strip()
    return [breed_name, min_weight, max_weight, colours]


def remove_breed():
    num = int(input("Enter number of the cat breed you want to remove: "))
    cat_breeds.pop(num - 1)


def filter_breed():
    opt = int(input("Enter number: 1 - filter by breed's name, 2 - filter by weight, 3 - filter by colour: "))
    search_criteria = input("Enter search criteria: ")
    filtered_breeds = []
    match opt:
        case 1:
            breed_name = "^" + search_criteria.lower().replace("*", ".*") + "$"
            regex = re.compile(breed_name)
            for breed in cat_breeds:
                if re.match(regex, breed[0].lower()):
                    filtered_breeds.append(breed)
        case 2:
            weight = int(search_criteria)
            for breed in cat_breeds:
                if breed[1] <= weight <= breed[2]:
                    filtered_breeds.append(breed)
        case 3:
            for breed in cat_breeds:
                if fnmatch.filter(breed[3], search_criteria):
                    filtered_breeds.append(breed)
    if len(filtered_breeds) > 0:
        print("Found these breeds: ")
        print_breeds(sorted(filtered_breeds, key=lambda x: x[0]))
    else:
        print("There are no breeds under your search criteria")


print("***********************CAT BREEDS CATALOG**********************************")

while True:
    print_info()
    opt = int(input())
    match opt:
        case 1:
            print_breeds()
        case 2:
            add_breed()
            print_breeds()
        case 3:
            edit_breed()
            print_breeds()
        case 4:
            remove_breed()
            print_breeds()
        case 5:
            filter_breed()
        case 6:
            exit(1)
