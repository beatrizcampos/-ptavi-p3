#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys


if __name__ == "__main__":
    try:
        fich = open(sys.argv[1], 'r')

    except IndexError: 
        print("Usage:  Python3 karaope.py file.smil")

  
