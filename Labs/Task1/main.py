#! /usr/bin/python
# main logic. Reverse array between first max element and last min
import sys
sys.path.append('../Utils')
import business
import ioutils

file = sys.argv[1]
arr = ioutils.read_array(file)
print ('Input was %s' % arr)
print ('Result was %s' % business.process(arr))
