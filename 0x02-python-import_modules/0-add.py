#!/usr/bin/python
from add_0 import add


def main():
    a = 1
    b = 2
    gut = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, gut))


if __name__ == "__main__":
    main()
