#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def find_searched(member):
        return member if member != search else replace
    return list(map(find_searched, my_list))
