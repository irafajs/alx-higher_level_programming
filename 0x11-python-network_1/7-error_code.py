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
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
