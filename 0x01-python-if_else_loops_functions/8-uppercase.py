#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range (97, 123):
            upper_ord = ord(i) - 32
        else:
            upper_ord = ord(i)

        print ('{}'.format(chr(upper_ord)), end='')
    print('\n',end='')
