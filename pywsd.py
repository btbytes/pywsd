#!/usr/bin/env python
'Generate Sequence Diagrams using websequencediagrams.com API.'

from __future__ import print_function
import os
import re
import urllib


def getSequenceDiagram(text, outputFile, style='default'):
    #adapted from http://www.websequencediagrams.com/embedding.html#python
    request = {}
    request["message"] = text
    request["style"] = style
    request["apiVersion"] = "1"

    url = urllib.urlencode(request)

    f = urllib.urlopen("http://www.websequencediagrams.com/", url)
    line = f.readline()
    f.close()

    expr = re.compile("(\?(img|pdf|png|svg)=[a-zA-Z0-9]+)")
    m = expr.search(line)

    if not m:
        print("Invalid response from server.")
        return False

    urllib.urlretrieve("http://www.websequencediagrams.com/" + m.group(0),
                       outputFile)
    return True

#traditional
STYLES = ['default', 'napkin', 'qsd', 'rose', 'mscgen', 'vs2010']
#colourful
STYLES += ['omegapple', 'modern-blue', 'earth', 'roungreen']

import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', metavar='INFILE', type=str,
        help='Input text containing sequence diagram instructions.')
    parser.add_argument('-o', action="store", dest="outfile",
        help='output file name. Default is .png')
    parser.add_argument('-s', action="store", dest="style",
        help='Options: ' + ','.join(STYLES))
    args = parser.parse_args()
    if args.style not in STYLES:
        args.style = 'default'
    fname, fext = os.path.splitext(os.path.basename(args.infile))
    outfile = args.outfile or '.'.join([fname, 'png'])
    style = args.style or 'default'
    with open(args.infile, 'r') as inp:
        text = inp.read()
    return 0 if getSequenceDiagram(text, outfile, style) else 1


if __name__ == '__main__':
    main()
