#!/usr/bin/python3
"""
this code gets the intranet url
"""
import requests

if __name__ == '__main__':
    link = "https://intranet.hbtn.io/status"
    anx = requests.get(link)
    text = anx.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
