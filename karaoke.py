#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import json
import urllib


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self, fich):

        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(fich)
        self.My_List = cHandler.get_tags()

    def __str__(self):

        resultado = ""
        for sublista in self.My_List:
            etiquetas = sublista[0]
            atributos = sublista[1]
            resultado += str(etiquetas + '\t')
            for clave in atributos:
                if atributos[clave]:
                    resultado = resultado + (str(clave + '="'
                                             + atributos[clave] + '"' + '\t'))
            resultado += "\n"
        return resultado

    def to_json(self, fich_name=""):

        if not fich_name:
            fich_name = "local.json"
        else:
            fich_name = fich_name.replace(".smil", ".json")
        with open(fich_name, 'w') as archivo_json:
            json.dump(self.My_List, archivo_json, indent=4,
                      separators=(' ', ': '), sort_keys=True)

    def do_local(self):
        for sublista in self.My_List:
            atributos = sublista[1]
            for clave in atributos:
                if atributos[clave].startswith('http://'):
                    urllib.request.urlretrieve(atributos[clave],
                                               atributos[clave].split('/')[-1])
                    atributos[clave] = atributos[clave].split('/')[-1]


if __name__ == "__main__":
    try:
        fich = open(sys.argv[1])

    except IndexError:
        print("Usage:  Python3 karaope.py file.smil")
    List = KaraokeLocal(fich)
    print(List)
    List.to_json(fich.name)
    List.do_local()
    List.to_json()
    print(List)
