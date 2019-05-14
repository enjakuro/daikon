#!/usr/bin/python
#-*- coding: utf-8 -*-
#Jasmin Engelmann
#11-747-334

import sys

filename = sys.argv[1]
infile = open(filename, 'r', encoding='utf-8')

#with open('dev.reversed.de', 'a', encoding='utf-8') as outfile:
#with open('dev.reversed.en', 'a', encoding='utf-8') as outfile:
#with open('test.reversed.de', 'a', encoding='utf-8') as outfile:
#with open('train.reversed.de', 'a', encoding='utf-8') as outfile:
#with open('train.reversed.en', 'a', encoding='utf-8') as outfile:
#with open('dev.trans.en', 'a', encoding='utf-8') as outfile:
with open('test.trans.en', 'a', encoding='utf-8') as outfile:

	for line in infile:
		line = line.split()
		line = reversed(line)
		line = " ".join(line)

		outfile.write(line)


infile.close()