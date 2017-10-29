import sys
import re

def main():
    with open(sys.argv[1], 'r') as content_file:
        pattern = r"([\S]+)\s([\S]+)\s\[(.*)\]\s\/(.*)\/"   # r makes the string raw
        for line in content_file:
            if line.startswith("#"):
                continue
            matches = re.search(pattern, line)
            for i in range(4):
                print(matches.group(i))
            break
            pass


if __name__ == "__main__":
    main()