#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import sys

ID_FIRST_FIELD = 0
ID_SECOND_FIELD = 0

if len(sys.argv) > 3: ID_FIRST_FIELD = int(sys.argv[3])
if len(sys.argv) > 4: ID_SECOND_FIELD = int(sys.argv[4])

for_remove = set([line.split('\t')[ID_SECOND_FIELD].strip() for line in open(sys.argv[2])])

for line in sys.stdin if sys.argv[1] == '--' else open(sys.argv[1]):
    id = line.split('\t')[ID_FIRST_FIELD].strip()
    if id in for_remove: sys.stderr.write(line)
    else: print line,
