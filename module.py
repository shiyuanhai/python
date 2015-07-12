#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Yuanhai Shi'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print("Hello,World")
	elif len(args)==2:
		print('Hello, %s' % args[1])
	else:
		print("Two many arguments!")

if __name__ == '__main__':
	test()

# private #
_xxx = 1
__xxx = 1