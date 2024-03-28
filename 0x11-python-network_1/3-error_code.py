#!/usr/bin/python3
"""
this code echoes response from a url
"""

if __name__ == "__main__":
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as ans:
            print(ans.read().decode('UTF-8'))
    except error.HTTPError as errors:
        print('Error code:', errors.code)
