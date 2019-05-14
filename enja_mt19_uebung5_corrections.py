#!/usr/bin/python
#-*- coding: utf-8 -*-
#Jasmin Engelmann
#11-747-334

import sys
import re

filename = sys.argv[1]
infile = open(filename, 'r', encoding='utf-8')

with open('test.postprocessed.en', 'a', encoding='utf-8') as outfile:

	for line in infile:
		line = re.sub(r' \.', r'. ', line)
		line = re.sub(r' @-@ ', r'-', line)
		line = re.sub(r'@@', r' ', line)

		outfile.write(line)


infile.close()