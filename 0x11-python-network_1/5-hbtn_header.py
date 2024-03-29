#!/usr/bin/python3
"""
this code accepts URL and sends req to get a response.
"""
import requests
from sys import argv

if __name__ == '__main__':
    ans = requests.get(argv[1])
    print(ans.headers.get('X-Request-Id'))
