#!/usr/bin/python3
"""
Shebang to make PY script
"""


if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
