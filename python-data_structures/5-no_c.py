#!/usr/bin/python3
# Can you C me now?
# Removes all c and C characters from a string
def no_c(my_string):
      copy = [e for e in my_string if e != 'c' and x != 'C']
      return("".join(copy))

