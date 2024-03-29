#!/usr/bin/python3
"""
this code gets https://intranet.hbtn.io/status url
"""
import requests

if __name__ == '__main__':
    link = "https://intranet.hbtn.io/status"
    xy = requests.get(link)
    text = xy.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
