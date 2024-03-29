#!/usr/bin/python3
"""
this code prints github info.
"""
import requests
from sys import argv

if __name__ == '__main__':
    link = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    ans = requests.get(link)
    commits = ans.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))

