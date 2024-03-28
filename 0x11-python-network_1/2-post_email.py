#!/usr/bin/python3
""" this code runs a POST request to get email and url result
"""

import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    link = sys.argv[1]
    info = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")

    info2 = urllib.request.Request(link, info)
    with urllib.request.urlopen(info2) as ans:
        print(ans.read().decode("utf-8"))
