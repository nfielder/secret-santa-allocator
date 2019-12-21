import json
from random import randint


def create_dictionary(names):
    d = {}
    for name in names:
        d[name] = None
    return d


def allocate(d, names):
    allocated = get_hard_allocation(d)
    for key in d.keys():
        if d[key] != None:
            continue
        available = names.copy()
        available.remove(key)
        for name in allocated:
            try:
                available.remove(name)
            except ValueError:
                pass

        r1 = randint(0, len(available)-1)
        d[key] = available[r1]
        allocated.append(available[r1])
    return d


def get_hard_allocation(d):
    arr = []
    for key in d.keys():
        if d[key] != None:
            arr.append(d[key])
    return arr


def create_hard_allocation(d):
    print("\nAvailable names are:", str(list(d.keys())))
    allocated = []

    option = ""
    while option.upper() != "F":
        option = input("Type in a name or (F)inish hard allocation: ")
        if option in d.keys():
            chosen_allocation = input("Choose person to allocate: ")
            if (chosen_allocation in d.keys()) and (chosen_allocation != option) and (chosen_allocation not in allocated):
                d[option] = chosen_allocation
                allocated.append(chosen_allocation)
                print("\n" + option, "was allocated", chosen_allocation + ".\n")
                continue
        elif option.upper() == "F":
            continue
        print("\nThat is not a valid allocation. Please try again.\n")


def select_mode():
    mode = input("Please select your mode: (G)enerate or (L)oad: ")
    if mode.upper() == "G":
        generate_mode()
    elif mode.upper() == "L":
        load_mode()
    else:
        print("\nThat isn't a valid option. Try again.\n")
        select_mode()


def generate_mode():
    names = input_names()
    unallocated_dict = create_dictionary(names)
    create_hard_allocation(unallocated_dict)
    allocated_dict = allocate(unallocated_dict, names)
    print("\n*** ALLOCATION COMPLETED! ***G\n")
    check_allocation(allocated_dict)


def check_allocation(d):
    option = ""
    while option.upper() != "Q":
        option = input("Enter your name or see (A)vailable names or (S)ave allocation or (Q)uit: ")
        if option in d.keys():
            print("\nYour allocated person is:", d[option], "\n")
        elif option.upper() == "A":
            print(f"Avaialable names are: {list(d.keys())}")
        elif option.upper() == "S":
            save_allocation(d)
        elif option.upper() == "Q":
            continue
        else:
            print("\nThat name is not in the allocation. Please check your spelling.\n")


def save_allocation(d):
    file_name = input("Please enter the filename to save your allocation to (including '.json'): ")
    json_str = json.dumps(d)
    with open(file_name, "w") as f:
        f.write(json_str)
    print(f"Allocation successfully saved as {file_name}.json")
    exit()


def input_names():
    while True:
        try:
            n = int(input("How many people are partaking in the secret santa? "))
            break
        except ValueError:
            print("\nThat is not a valid integer. Please try again.\n")

    names = []
    i = 0
    while i < n:
        name = input("Enter the name of person " + str(i+1) + ": ")
        if name not in names:
            names.append(name)
            i += 1
        else:
            print("\nName must be unique! Maybe add the initial of a surname?\n")

    return names


def load_mode():
    file_name = input("Enter the file name of the file you want to load (including '.json'): ")
    with open(file_name) as f:
        json_str = f.read()
    d = json.loads(json_str)
    print(f"\nLoaded allocation from {file_name}.")
    check_allocation(d)


def print_introduction():
    print("\nWelcome to the Secret Santa Allocator!\n")
    print("This program allows easy allocation of individuals for the classic secret santa format.")
    print("The program has two modes: Generate and Load.")
    print("-Generate will go through the process of a creating a new allocation.")
    print("-Load will reload an existing allocation.\n")


def main():
    print_introduction()
    select_mode()


if __name__ == "__main__":
    main()
