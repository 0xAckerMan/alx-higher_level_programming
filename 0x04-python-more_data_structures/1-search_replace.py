#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''
    Works well too
    return [replace if x == search else x for x in my_list]'''
    new_list = my_list.copy()
    for x in new_list:
        if x == search:
            new_list[x] = replace
    return new_list
