#!/usr/bin/python3
"""
Shebang to make PY script
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
        sys.exit(1)

    except urllib.error.URLError as e:
        print(f"Error: {e}")
        sys.exit(1)
