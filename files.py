#!/usr/bin/env python

'''

A script to load files from a folder

'''

import json
import os
import sys

def main(folder):

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    for file in files:
        location = os.path.join(folder, file)
        try:
            raw = open(location, 'r').read()

            # do something
        except:
            pass


if __name__ == "__main__":

    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print 'Usage: %s <folder containing files>' % sys.argv[0]
