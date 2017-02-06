#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import sys
from collections import Counter

fin = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

res = Counter()

for i, line in enumerate(fin):
    res[line.strip()] += 1
    if i % 100000 == 0: sys.stderr.write("%s\n" % i)

for item, freq in res.most_common():
    print "%s\t%s" % (item, freq)

