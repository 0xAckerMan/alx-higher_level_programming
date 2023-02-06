#!/usr/bin/python3
''' Defines the lookup function'''


def lookup(obj):
    '''Function implementation with obj arg'''
    return [i for i in dir(obj)]
