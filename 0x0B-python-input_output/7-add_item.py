#!/usr/bin/python3

"""Module 7-add_item
Adds python script arguments to a JSON file
"""

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    import sys
    arg_list = sys.argv

    try:
        new_list = load_from_json_file("add_item.json")
    except FileNotFound:
        new_list = []
    for i in range(1, len(arg_list)):
        new_list.append(arg_list[i])

    save_to_json_file(new_list, "add_item.json")
