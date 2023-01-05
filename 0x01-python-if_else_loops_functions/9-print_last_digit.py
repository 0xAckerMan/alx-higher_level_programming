#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    c = number % 10
    print ('{}'.format(c), end='')
    return c
