#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    mytup_a = tuple_a
    mytup_b = tuple_b

    return (mytup_a, mytup_b)
