#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Prints the first 'x' elements of a list and only integers
def safe_print_list_integers(my_list=[], x=0):

    a = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            a += 1
        except (ValueError, TypeError):
            continue
        print("")
        return a
if __name__ == "2-main":
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
