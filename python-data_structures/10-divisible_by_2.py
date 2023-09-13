#!/usr/bin/python3
# 10-divisible_by_2.py
# Finds all multiples of 2
def divisible_by_2(my_list=[]):
     my_list = []
      for i in range(len(my_list)):
          if my_list[i] % 2 == 0:
              my_list.append(True)
            else:
                my_list.append(False)

            return (my_list)
