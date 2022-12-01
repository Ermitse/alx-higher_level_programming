#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    add = 0
    for i in range(argc):
        add += int(sys.argv[i + 1])
    print(add)
