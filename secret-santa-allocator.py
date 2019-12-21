from random import randint


def create_dictionary(names):
    d = {}
    for name in names:
        d[name] = None
    return d


def allocate(d, names):
    d["Julia"] = "Megan"
    allocated = ["Megan"]
    for key in d.keys():
        if key == "Julia":
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


def main():
    names = ["Nathan", "Justin", "Julia", "Finlay", "Megan"]
    unallocated_dict = create_dictionary(names)
    allocated_dict = allocate(unallocated_dict, names)

    option = ""
    while option.upper() != "Q":
        option = input("Enter your name or (Q)uit: ")
        if option in allocated_dict.keys():
            print("\nYour allocated person is:", allocated_dict[option], "\n")


if __name__ == "__main__":
    main()
