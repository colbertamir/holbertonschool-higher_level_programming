#!/usr/bin/python3
# 8-multiple_returns.py
# Returns a tuple with the length of a string and its first character
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
     return (len(sentence), sentence[0])
