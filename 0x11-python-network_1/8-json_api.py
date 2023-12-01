#!/usr/bin/python3
"""
Shebang to make PY script
"""


if __name__ == '__main__':
    import requests
    import sys

    q = "" if len(sys.argv) < 2 else sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    response = requests.post(url, data=data)
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
