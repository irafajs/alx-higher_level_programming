#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    hi_name = dir(hidden_4)
    count = len(hi_name)
    for l_count in range(count):
        if (hi_name[l_count][0] != '_'):
            print("{}".format(hi_name[l_count]))
