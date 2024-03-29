#!/usr/bin/python3
"""
this code gets https://intranet.hbtn.io/status url
"""
import requests

if __name__ == '__main__':
    anx = requests.get("https://intranet.hbtn.io/status")
    inpt = anx.text
    print("Body response:")
    print("\t- type: {}".format(type(inpt)))
    print("\t- content: {}".format(inpt))
