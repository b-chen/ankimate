#!/usr/bin/python3
import sys
import re


def write_card(desc, ch, pinyin, output_file):
    full_desc = re.sub(r"\d", '', pinyin) + " " + desc
    line = full_desc + ", " + ch + ", " + pinyin + "\n"
    output_file.write(line)

def main():
    if len(sys.argv) != 3:
        print("Not enough arguments")

    simp = {}
    trad = {}
    with open(sys.argv[1], 'r') as dict_file:
        pattern = r"([\S]+)\s([\S]+)\s\[(.*)\]\s\/(.*)\/"  # r makes the string raw

        # read in dictionary
        for line in dict_file:
            if line.startswith("#"):
                continue
            matches = re.search(pattern, line)

            # 1 is traditional
            # 2 is simplified
            # 3 is pinyin
            # 4 is definition
            pinyin_eng = (matches.group(3), matches.group(4))
            simp[matches.group(1)] = pinyin_eng
            trad[matches.group(2)] = pinyin_eng

    # read in file and make flashcard
    #print(simp)
    with open(sys.argv[2], 'r') as content_file, open(sys.argv[2] + ".out", 'x', encoding="utf-8") as output_file:
        for i, line in enumerate(content_file):
            line = line.rstrip()
            if line in simp:
                write_card(simp[line][1], line, simp[line][0], output_file)
            elif line in trad:  # write flash card
                write_card(trad[line][1], line, trad[line][0], output_file)
            else:
                print("line " + str(i) + ": " + line + " not found in dictionary")


if __name__ == "__main__":
    main()
