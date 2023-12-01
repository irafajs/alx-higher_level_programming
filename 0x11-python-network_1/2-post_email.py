#!/usr/bin/python3
"""
Shebang to make PY script
"""


if __name__ == '__main__':
    import urllib.request
    import sys

    if len(sys.argv) != 3:
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        content = response.read()
        print(content.decode('utf-8'))
