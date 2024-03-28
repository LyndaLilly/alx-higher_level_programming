#!/usr/bin/python3
"""this code gets the URL from command-line arguments"""

import urllib.request
import sys


if __name__ == "__main__":
    link = sys.argv[1]

    req = urllib.request.Request(link)
    with urllib.request.urlopen(req) as ans:
        print(dict(ans.headers).get("X-Request-Id"))
