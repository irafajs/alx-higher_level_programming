#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    check_tuple_a = tuple_a[:2] + (0, 0)
    check_tuple_b = tuple_b[:2] + (0, 0)
    sum_0 = check_tuple_a[0] + check_tuple_b[0]
    sum_1 = check_tuple_a[1] + check_tuple_b[1]
    result = sum_0, sum_1
    return result
