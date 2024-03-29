#!/usr/bin/python3
"""
this code accepts letter and make a POST request to
http://0.0.0.0:5000/search_user.
"""
import requests
from sys import argv

if __name__ == '__main__':
    xy = argv[1] if len(argv) == 2 else ""
    link = 'http://0.0.0.0:5000/search_user'
    ans = requests.post(link, data={'xy': xy})
    try:
        ans2 = ans.json()
        id, name = ans2.get('id'), ans2.get('name')
        if len(ans2) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(ans2.get('id'), ans2.get('name')))
    except Exception:
        print("Not a valid JSON")
