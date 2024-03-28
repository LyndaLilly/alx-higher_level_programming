#!/usr/bin/python3
"""the code gets data from alx-intranet url
"""

import urllib.request

link = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(link) as ans:
    body = ans.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
