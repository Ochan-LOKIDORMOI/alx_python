#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Use the "&" operator to find the common elements in the two sets
    common_set = set_1 & set_2
    return common_set