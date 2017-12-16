#!/usr/bin/env python3

import sys
import os
import dynamo

USAGE = '''
dynamo <input-file> <output-file>
'''


def main():
    if len(sys.argv) != 3:
        print(USAGE)
        exit()

    input_file, output_file = sys.argv[1:]
    dynamo.compile(input_file, output_file)
    print('OK')

if __name__ == '__main__':
    main()
