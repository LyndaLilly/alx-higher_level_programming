#!/usr/bin/python3
"""
this code accepts link and an email address,
and make a POST request to get result.
"""
from sys import argv
import requests

if __name__ == '__main__':
    lm = {'email': argv[2]}
    ans = requests.post(argv[1], data=lm)
    print(ans.text)
