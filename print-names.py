def print_names(register):
    for names in register:
        if isinstance(names, str):
            print(names)

register = [1, 2, 3, "Ade", "Bola", "Joseph"]


print_names(register)