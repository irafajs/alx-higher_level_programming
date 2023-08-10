#!/usr/bin/python
import add_0


def main():
    a = 1
    b = 2
    gut = add_0.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, gut))


if __name__ == "__main__":
    main()
