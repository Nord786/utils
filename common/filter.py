#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

"""
argv[1] - данные для фильтрации
argv[2] - фильтр (хорошие запросы)
"""

import sys

ID_FIRST_FIELD = 0
ID_SECOND_FIELD = 0
SEPARATOR = '\t'

if len(sys.argv) > 3: ID_FIRST_FIELD = int(sys.argv[3])
if len(sys.argv) > 4: ID_SECOND_FIELD = int(sys.argv[4])
if len(sys.argv) > 5: SEPARATOR=sys.argv[5]

for_filter = set([line.split(SEPARATOR)[ID_SECOND_FIELD].strip() for line in open(sys.argv[2])])

for line in sys.stdin if sys.argv[1] == '--' else open(sys.argv[1]):
    id = line.split(SEPARATOR)[ID_FIRST_FIELD].strip()
    if id not in for_filter: 
        sys.stderr.write(line)
        pass 
    else: print line,
