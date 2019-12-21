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


def main():
    names = ["Nathan", "Justin", "Julia", "Finlay", "Megan"]
    unallocated_dict = create_dictionary(names)
    unallocated_dict["Julia"] = "Megan"
    allocated_dict = allocate(unallocated_dict, names)

    option = ""
    while option.upper() != "Q":
        option = input("Enter your name or (Q)uit: ")
        if option in allocated_dict.keys():
            print("\nYour allocated person is:", allocated_dict[option], "\n")
        elif option.upper() == "Q":
            continue
        else:
            print("\nThat name is not in the allocation. Please check your spelling.\n")


if __name__ == "__main__":
    main()
