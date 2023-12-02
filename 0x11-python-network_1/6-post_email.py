#!/usr/bin/python3
"""
Shebang to make PY script
"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    response = requests.post(url, data=data)
    print(f"Your email is: {request.text}")
