#!/usr/bin/python3
"""
this code prints github info.
"""
import requests
from sys import argv

if __name__ == '__main__':
    link = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    ans = requests.get(link)
    infos = ans.json()
    for xy in infos[:10]:
        print(xy.get('sha'), end=': ')
        print(xy.get('xy').get('author').get('name'))
