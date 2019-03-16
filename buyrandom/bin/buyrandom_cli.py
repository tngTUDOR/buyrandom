#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generic executable.

This documentation defines how the program is run; see http://docopt.org/.

Commands:

Arguments:
    SEED optional random input seed

Usage:
    buyrandom-cli SEED

Options:

"""

from docopt import docopt
from buyrandom.worker import get_statement
import sys
import os

def main():
    try:
        args = docopt(__doc__, version='0.1.1')
        if len(args) == 0:
            random_data = os.urandom(8)
            seed = int.from_bytes(random_data, byteorder="big")
        if len(args) == 1:
            try:
                seed = int(args['SEED'])
            except:
                #TODO: treat exception
                return
        s = get_statement(seed)
        print(s)
    except KeyboardInterrupt:
        print("Terminating CLI")
        sys.exit(1)


if __name__ == "__main__":
    main()
