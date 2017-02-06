#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import sys
import random



lines = sys.stdin.readlines()
random.shuffle(lines)
if len(sys.argv) > 1: sys.stdout.writelines( lines[:int(sys.argv[1])] )
else: sys.stdout.writelines(lines)
