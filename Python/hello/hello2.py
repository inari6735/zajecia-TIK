#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hello2.py

import hello

def main(args):
    hello.witaj()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
