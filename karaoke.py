#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import json

def listado(lista):

    for sublista in lista:
        etiquetas = sublista[0]
        atributos = sublista[1]
        resultado = str(etiquetas + '\t')        
        for clave in atributos:
            if atributos[clave]:
                resultado = resultado + (str(clave + '="' + atributos[clave] + '"' + '\t'))
        print(json.dump(resultado))    

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
