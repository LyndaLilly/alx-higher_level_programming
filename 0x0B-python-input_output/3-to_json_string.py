#!/usr/bin/python3
"""meaning of string-to-JSON func"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
