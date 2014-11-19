#!/bin/python
#get the mean and std of a bunch of numbers

from csvHandle import *
from calc import *
import sys

if len(sys.argv) <= 1:
	print 'No file'
	exit()


tmp = convert(sys.argv[1]);
print tmp
