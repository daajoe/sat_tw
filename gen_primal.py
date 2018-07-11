#!/usr/bin/env python2.7
import argparse
import sys
import os

import gzip
from bz2 import BZ2File
from itertools import count, izip
import backports.lzma as xz

import mimetypes

from itertools import imap

def read_fromfile(filename):
    try:
        stream = None
        mtype = mimetypes.guess_type(filename)[1]
        if mtype is None:
            stream = open(filename, 'r')
        elif mtype == 'bzip2':
            stream = BZ2File(filename, 'r')
        elif mtype == 'gz':
            stream = gzip.open(filename, 'r')
        elif mtype == 'xz':
            stream = xz.open(filename, 'r')
        else:
            raise IOError('Unknown input type "%s" for file "%s"' % (mtype, filename))
        numVariables = 0
        for line in stream:
            line = line.split()
            if line == [] or line[0] in ('c', 'n'):
                continue
            if line[0] == 'p':
                num_vars = int(line[2])
                num_cls = int(line[3])
                print 'p tw %s %s'%(num_vars,num_cls)
            else:
                print ' '.join(imap(lambda x: str(abs(int(x))), line[:-1]))

    finally:
        if stream:
            stream.close()
                                                  

def parse_args():
    parser = argparse.ArgumentParser(description='%(prog)s -f instance')
    # parser.formatter_class._max_help_position = 120
    parser.add_argument('-f', '--file', dest='instance', action='store', type=lambda x: os.path.realpath(x),
                                                       help='instance')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    filename = args.instance
    print filename
    read_fromfile(filename)


main()
