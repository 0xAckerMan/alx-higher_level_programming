#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print('0 arguments.')
elif len(argv) == 2:
    print('1 argument:')
    print(f'{len(argv)-1:d}: {argv[len(argv)-1]:d}')
else:
    print(f"{len(argv)-1:d} arguments:")
    for i in range(1, len(argv)):
        print(f'{i:d}: {argv[i]:s}')
