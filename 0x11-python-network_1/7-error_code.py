#!/usr/bin/python3
"""
this code accepts link and an email address,
and make a POST request to get result.
"""
from sys import argv
import requests

if __name__ == '__main__':
    ans = requests.get(argv[1])
    curr = ans.status_code
    print(ans.text) if curr < 400 else print(
        "Error code: {}".format(ans.status_code))
