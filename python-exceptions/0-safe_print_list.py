#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    full_len = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            full_len += 1
        except IndexError:
            break

    print()
    return full_len
