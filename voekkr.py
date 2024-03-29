#!/usr/bin/env python3
"""Generate random voekkrs"""

import argparse
import random

import pyfiglet


def parse():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description="generate random voekkrs")
    parser.add_argument(
        "length", type=int, nargs="?", help="length of voekkr to generate"
    )
    parser.add_argument("-a", "--ascii", action="store_true", help="output ascii art")
    return parser.parse_args()


def main():
    """Main function"""
    args = parse()
    vokkor_length = -1 if not args.length else args.length - 4
    while vokkor_length < 2:
        vokkor_length = int(input("Voekkr length? ")) - 4

    string = ["e" if random.randint(0, 1) == 0 else "o" for _ in range(vokkor_length)]

    for letter in ["e", "o"]:
        if letter not in string:
            idx_letter = random.randint(0, vokkor_length - 1)
            string[idx_letter] = letter

    idx_k1 = random.randint(0, vokkor_length)
    idx_k2 = random.randint(0, vokkor_length)
    string.insert(idx_k1, "k")
    string.insert(idx_k2, "k")

    if args.ascii:
        print(pyfiglet.figlet_format(f"v{''.join(string)}r"))
    else:
        print(f"v{''.join(string)}r")


if __name__ == "__main__":
    main()
