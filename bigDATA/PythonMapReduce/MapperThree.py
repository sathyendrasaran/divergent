#!/usr/bin/env python

import sys
import csv

SEP = "," #easy to change separator

class Mapper(object):

    def __init__(self, stream, sep=SEP):
        self.stream = stream
        self.sep = SEP

    def emit(self, key, value):
        sys.stdout.write("{0}{1}{2}\n".format(key, self.sep, value))

    def map(self):
        for row in self:
            self.emit(row[3]+"-"+row[4], row[8])

    def __iter__(self):
        reader = csv.reader(self.stream)
        for row in reader:
            yield row


if __name__ == "__main__":
    mapper = Mapper(sys.stdin)
    mapper.map()

