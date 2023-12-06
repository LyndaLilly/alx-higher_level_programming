#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == p else p for p in my_list]
