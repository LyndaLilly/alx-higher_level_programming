#!/usr/bin/python3
"""
this code prints data from github api.
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    link = 'https://api.github.com/users/{}'.format(argv[1])
    ans = requests.get(link,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(ans.json().get('id'))
