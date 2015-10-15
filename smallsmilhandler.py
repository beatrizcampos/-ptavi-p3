#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    """
    Etiquetas y atributos que debe reconocer:

    root-layout (width, height, background-color)
    region (id, top, bottom, left, right)
    img (src, region, begin, dur)
    audio (src, begin, dur)
    textstream (src, region
    """

if __name__ == "__main__":
    """
    Programa principal
    """
