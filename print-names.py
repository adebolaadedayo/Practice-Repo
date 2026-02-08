#A new function to print only actual names in a register
def print_names(register):
    for names in register:
        if isinstance(names, str):
            print(names)
#Register 1
register = [1, 2, 3, "Ade", "Bola", "Joseph"]


print_names(register)

#Register 2
new_register = ["Waliba", "Ahmed"]
print_names(new_register)