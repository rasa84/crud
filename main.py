cat_breeds = [
    [
        "Abyssinian",
        6,
        10,
        ["Ruddy", "red", "blue", "fawn"],
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
    print("5. Exit")
    print("*****************************************************")


def print_breed(breed, num):
    colour = ""
    for b in breed[3]:
        colour += b + ", "
    print(f"{num}. Cat breed name: {breed[0]}. Weight: {breed[1]}-{breed[2]}. Colours: {colour[:-2]}.")


def print_breeds():
    count = 1
    for b in cat_breeds:
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
            exit(1)
