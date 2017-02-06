#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import sys

fin = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

res = set()

for i, line in enumerate(fin, 1):
    hash_line = hash(line)
    if not hash_line in res: 
        res.add(hash_line)
        print line,
    if i % 100000 == 0: sys.stderr.write("%s\n" % i)
