#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list

    for i in range(len(my_list)):
        if i == my_list[idx]:
            my_list.remove(i)
    return my_list
