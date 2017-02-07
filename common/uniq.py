#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import sys

fin = sys.stdin

TRACE_NUM_DEFAULT = 100000
TRACE_NUM = int(sys.argv[1]) if len(sys.argv) > 1 else TRACE_NUM_DEFAULT

res = set()

for i, line in enumerate(fin, 1):
    hash_line = hash(line)
    if not hash_line in res: 
        res.add(hash_line)
        print line,
    if TRACE_NUM > 0 and  i % TRACE_NUM == 0: sys.stderr.write("%s\n" % i)
