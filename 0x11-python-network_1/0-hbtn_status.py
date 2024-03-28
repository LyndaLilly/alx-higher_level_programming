#!/usr/bin/python3
"""the code gets data from alx-intranet url
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as ans:
    body = ans.read().decode('utf-8')
    print("- Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
