#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return

    for item in range(1, len(my_list) + 1):
        print('{:d}'.format(my_list[-item]))
