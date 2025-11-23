#!/usr/bin/env python
"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)

    top3 = []

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for _, count in group)

            top3.append((total_count, current_word))

            top3 = sorted(top3, key=lambda x: x[0], reverse=True)[:3]

        except ValueError:
            pass

    for count, word in top3:
        print(f"{word}{separator}{count}")

if __name__ == "__main__":
    main()
