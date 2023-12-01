#!/usr/bin/python3
"""
Shebang to make PY script
"""


if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 3:
        sys.exit(1)

    username = sys.argv[1]
    key_word = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.post(url, auth=(username, key_word))
    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(None)
