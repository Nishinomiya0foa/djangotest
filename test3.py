# -*- coding:utf-8 -*-
'a test module'
__author__ = 'abc'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print(args)
        print('%s 的长度为：1' % args)
    else:
        print('%s 的长度为：%d' % (args, len(args)))

if __name__ == '__main__':
    test()