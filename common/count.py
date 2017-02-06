#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

from __future__ import division

import sys
from collections import Counter

fin = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin

res = Counter() 

for i, line in enumerate(fin):
    res[line.strip()] += 1
    if i % 100000 == 0: sys.stderr.write("%s\n" % i)

total = sum(res.values())

for line, freq in res.most_common():
    print "%s\t%s\t%s" % (line, freq, freq/total)

