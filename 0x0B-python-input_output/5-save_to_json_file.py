#!/usr/bin/python3
'''
Writes an object to a file using json representation
'''
import json


def save_to_json_file(my_obj, filename):
    '''The func implementation'''

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
