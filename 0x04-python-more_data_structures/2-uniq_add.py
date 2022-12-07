#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for member in set(my_list):
        sum += member
    return sum

