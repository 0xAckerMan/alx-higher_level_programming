#!/usr/bin/python3
'''Class that inherits from another one'''


class MyList(list):
    '''Child class implementation that inherits from list'''

    def print_sorted(self):
        '''prints a sorted list'''
        print(sorted(self))
