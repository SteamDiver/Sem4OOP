#! /usr/bin/python
# main logic. Reverse array between first max element and last min
import sys
sys.path.append('../Utils')
import business
import ioutils
import my_parser

file = my_parser.create_parser().parse_args().name
arr = ioutils.read_array(file)
print ('Inp was %s' % arr)
print ('Res was %s' % business.solve(arr))
