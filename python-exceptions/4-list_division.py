#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    for i in range(list_length):
        try:
            div = 0
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                if my_list_2[i] != 0:
                    div = my_list_1[i] / my_list_2[i]
                else:
                    print("division by 0")
            else:
                print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div)
    return new_list

if __name__ == "__main__":
     my_l_1 = [10, 8, 4]
     my_l_2 = [2, 4, 4]
     result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
     print(result)

     print("--")

     my_l_1 = [10, 8, 4, 4]
     my_l_2 = [2, 0, "H", 2, 7]
     result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
     print(result)
