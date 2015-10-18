#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.dicc = {'root-layout': ['width', 'height', 'background-color'],
                     'region': ['id', 'top', 'bottom', 'left', 'right'],
                     'img': ['src', 'region', 'begin', 'dur'],
                     'audio': ['src', 'begin', 'dur'],
                     'textstream': ['src', 'region']}

        self.list = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name in self.dicc:
            newdicc = {}
            for atribute in self.dicc[name]:
                newdicc[atribute] = attrs.get(atribute, "")
            self.list.append([name, newdicc])

    def get_tags(self):

        return self.list

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    My_List = cHandler.get_tags()
    print(My_List)
