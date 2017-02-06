#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

"""
argv[1] - данные для фильтрации
argv[2] - фильтр (хорошие запросы)
"""

import sys

ID_FIRST_FIELD = 0
ID_SECOND_FIELD = 0
DEFAULT_VALUE = ''
SEPARATOR = '\t'

if len(sys.argv) > 3: ID_FIRST_FIELD = int(sys.argv[3])
if len(sys.argv) > 4: ID_SECOND_FIELD = int(sys.argv[4])
if len(sys.argv) > 5: DEFAULT_VALUE=sys.argv[5]
if len(sys.argv) > 6: SEPARATOR=sys.argv[5]

for_join = {}
for line in open(sys.argv[2]):
    data = line.strip().split(SEPARATOR)
    key = data.pop(ID_SECOND_FIELD)
    for_join[key] = data

for line in open(sys.argv[1]):
    data = line.strip().split(SEPARATOR)
    key = data[ID_FIRST_FIELD]
    if key in for_join:
        data.extend(for_join[key])
    else:
        sys.stderr.write("NO_JOIN\t%s" % line)
        #Если указанное DEFAULT_VALUE, то добавляем его - иначе пропускаем строку
        if DEFAULT_VALUE: data.append(DEFAULT_VALUE)
        else: continue
    print '\t'.join(data)
