#!/usr/bin/python3
"""
Shebang to make PY script
"""


if __name__ == '__main__':
    import urllib.request
    import sys

    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        if 'X-Request-Id' in headers:
            x_request_id = headers['X-Request-Id']
            print("X-Request-Id:", x_request_id)
