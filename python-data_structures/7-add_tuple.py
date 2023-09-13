#!/usr/bin/python3
# 7-add_tuple.py
# Add two tuples
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = tuple_a + tuple_b

    for i in range(len(tuple_a)):
        tuple_sum.append(tuple_a[i])
    else:
        tuple_sum[i] += tuple_b[i]

        return tuple_sum
