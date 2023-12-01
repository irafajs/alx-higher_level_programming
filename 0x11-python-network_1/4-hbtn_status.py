#!/usr/bin/python3
"""
Shebang to make PY script
"""


if __name__ == '__main__':
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
