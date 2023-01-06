#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print('0 arguments.')
elif len(argv) == 2:
    print('1 argument:')
    print(f'{len(argv)-1}: {argv[len(argv)-1]}')
else:
    print(f"{len(argv)-1} arguments:")
    for i in range(1, len(argv)):
        print(f'{i}: {argv[i]:s}')
