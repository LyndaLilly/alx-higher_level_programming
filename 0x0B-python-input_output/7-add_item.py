#!/usr/bin/python3
"""computes  Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        xt = load_from_json_file("add_item.json")
    except FileNotFoundError:
        xt = []
    xt.extend(sys.argv[1:])
    save_to_json_file(xt, "add_item.json")
