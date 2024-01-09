#!/usr/bin/python3
# 6-from_json_string.py
"""meaning of JSON-to-object func."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
