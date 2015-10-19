#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import json
import urllib


def listado(lista):

    for sublista in lista:
        etiquetas = sublista[0]
        atributos = sublista[1]
        resultado = str(etiquetas + '\t')
        for clave in atributos:
            if atributos[clave]:
                resultado = resultado + (str(clave + '="'
                                         + atributos[clave] + '"' + '\t'))
        print(resultado)


def do_local(lista):
    for sublista in lista:
        atributos = sublista[1]
        for clave in atributos:
            if atributos[clave].startswith('http://'):
                urllib.request.urlretrieve(atributos[clave],
                                           atributos[clave].split('/')[-1])


def to_json(My_List, fich_name=""):

    if not fich_name:
        fich_name = "local.json"
    else:
        fich_name = fich_name.replace(".smil", ".json")
    with open(fich_name, 'w') as archivo_json:
        json.dump(My_List, archivo_json, indent=4,
                  separators=(' ', ': '), sort_keys=True)

if __name__ == "__main__":
    try:
        fich = open(sys.argv[1])

    except IndexError:
        print("Usage:  Python3 karaope.py file.smil")

    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(fich)
    My_List = cHandler.get_tags()
    List = listado(My_List)
    to_json(My_List, fich.name)
    do_local(My_List)
