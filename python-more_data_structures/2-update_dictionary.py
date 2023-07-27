#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # If the key exists in the dictionary, update its value
    if key in a_dictionary:
        a_dictionary[key] = value
    # If the key doesn't exist in the dictionary, add it with the given value
    else:
        a_dictionary[key] = value
    return a_dictionary